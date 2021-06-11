import psutil
from PyQt5.QtWidgets import QDialog, QMessageBox, QTreeWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from ui.CreatePlotDialog import Ui_CreatePlotDialog
from core.plot import PlotTask, PlotSubTask
from config import get_config, save_config
import os
from utils import make_name, size_to_str, get_k_size, get_k_temp_size, get_fpk_ppk, get_official_chia_exe, seconds_to_str
from datetime import datetime
from core.disk import get_disk_usage
from PyQt5.QtWidgets import QFileDialog
from core import BASE_DIR, is_debug
import platform
from typing import Optional
from core.plotter import PLOTTER_OFFICIAL, PLOTTER_BUILTIN, PLOTTER_CHIA_PLOT


class CreatePlotDialog(QDialog, Ui_CreatePlotDialog):
    last_ssd_folder = ''
    last_hdd_folder = ''

    def __init__(self, task: Optional[PlotTask] = None, auto=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.result = []
        self.task = None
        self.batch_tasks = []

        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.treeWidgetTasks.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        config = get_config()

        self.buttonBox.button(self.buttonBox.Ok).setText('创建')
        self.buttonBox.button(self.buttonBox.Cancel).setText('取消')
        self.checkBoxSpecifyCount.stateChanged.connect(self.check_specify_count)
        self.commandLinkButton.clicked.connect(self.about_public_key)
        self.spinNumber.valueChanged.connect(self.update_tip_text)

        self.comboK.addItem('101.4GiB (k=32, 临时文件: 239GiB)', 32)
        self.comboK.addItem('208.8GiB (k=33, 临时文件: 521GiB)', 33)
        self.comboK.addItem('429.8GiB (k=34, 临时文件: 1041GiB)', 34)
        self.comboK.addItem('884.1GiB (k=35, 临时文件: 2175GiB)', 35)
        self.comboK.setCurrentIndex(0)

        self.comboCmdLine.addItem('使用多线程chia_plot.exe', self.get_chia_plot_exe())
        self.comboCmdLine.setCurrentIndex(0)

        self.comboCmdLine.addItem('使用内置ProofOfSpace.exe', self.get_builtin_exe())
        self.comboCmdLine.setCurrentIndex(1)

        chia_exe = get_official_chia_exe()
        if chia_exe:
            self.comboCmdLine.addItem('使用钱包chia.exe', chia_exe)
            self.comboCmdLine.setCurrentIndex(self.comboCmdLine.count()-1)

        # self.comboCmdLine.addItem('手动选择', 'select')
        self.comboCmdLine.currentIndexChanged.connect(self.change_cmdline)
        self.change_cmdline()

        def select_cmdline(cmdline):
            for i in range(self.comboCmdLine.count()):
                d = self.comboCmdLine.itemData(i, Qt.UserRole)
                if d == cmdline:
                    self.comboCmdLine.setCurrentIndex(i)
                    return

            if task:
                self.comboCmdLine.addItem(os.path.basename(cmdline), cmdline)
                self.comboCmdLine.setCurrentIndex(self.comboCmdLine.count()-1)
                self.lineEditCmdLine.setText(cmdline)

        def select_k_combo(k):
            for i in range(self.comboK.count()):
                d = self.comboK.itemData(i, Qt.UserRole)
                if d == k:
                    self.comboK.setCurrentIndex(i)
                    return

        self.modify = False

        if task:
            self.task = task
            self.modify = True

            self.comboSSD.addItem(task.ssd_folder, task.ssd_folder)
            self.comboSSD.setDisabled(True)

            current_index = 0
            self.comboHDD.addItem('自动', 'auto')
            for hdd_folder_obj in config['hdd_folders']:
                folder = hdd_folder_obj['folder']
                text = folder
                if os.path.exists(folder):
                    usage = get_disk_usage(folder)
                    text += f" ({size_to_str(usage.free)}空闲)"
                else:
                    text += " (不存在)"
                if folder == task.hdd_folder:
                    current_index = self.comboHDD.count()
                self.comboHDD.addItem(text, folder)
            if self.task.auto_hdd_folder:
                self.comboHDD.setCurrentIndex(0)
            else:
                self.comboHDD.setCurrentIndex(current_index)

            self.editFpk.setPlainText(task.fpk)
            self.editFpk.setDisabled(True)
            self.editPpk.setPlainText(task.ppk)
            self.editPpk.setDisabled(True)

            self.checkBoxSpecifyCount.setChecked(task.specify_count)
            self.checkBoxSpecifyCount.setDisabled(True)
            self.spinNumber.setValue(task.count)
            self.spinNumber.setDisabled(True)

            self.spinThreadNum.setValue(task.number_of_thread)
            self.spinMemory.setValue(task.memory_size)

            self.timeEditDelay.setDisabled(True)

            self.spinBucketNum.setValue(task.buckets)
            select_k_combo(task.k)
            self.checkBoxNoBitfield.setChecked(task.nobitfield)
            select_cmdline(task.cmdline)

            self.setWindowTitle('编辑P图任务')

            self.buttonBox.button(self.buttonBox.Ok).setText('修改')
        else:
            self.comboSSD.addItem('自动', 'auto')
            current_index = 0
            if not auto:
                current_index = 1
            for ssd_folder in config['ssd_folders']:
                text = ssd_folder
                if os.path.exists(ssd_folder):
                    usage = get_disk_usage(ssd_folder)
                    text += f" ({size_to_str(usage.free)}空闲)"
                else:
                    text += " (不存在)"
                if not auto and ssd_folder == CreatePlotDialog.last_ssd_folder:
                    current_index = self.comboSSD.count()
                self.comboSSD.addItem(text, ssd_folder)
            self.comboSSD.setCurrentIndex(current_index)

            current_index = 0
            self.comboHDD.addItem('自动', 'auto')
            for hdd_folder_obj in config['hdd_folders']:
                folder = hdd_folder_obj['folder']
                text = folder
                if os.path.exists(folder):
                    usage = get_disk_usage(folder)
                    text += f" ({size_to_str(usage.free)}空闲)"
                else:
                    text += " (不存在)"
                if folder == CreatePlotDialog.last_hdd_folder:
                    current_index = self.comboHDD.count()
                self.comboHDD.addItem(text, folder)
            self.comboHDD.setCurrentIndex(current_index)

            fpk = ''
            ppk = ''
            if 'fpk' in config:
                fpk = config['fpk']

            if 'ppk' in config:
                ppk = config['ppk']

            if not fpk and not ppk and chia_exe:
                fpk, ppk = get_fpk_ppk(chia_exe)

            self.editFpk.setPlainText(fpk)
            self.editPpk.setPlainText(ppk)

            if 'num' in config:
                self.spinNumber.setValue(config['num'])

            if 'thread_num' in config:
                self.spinThreadNum.setValue(config['thread_num'])

            if 'memory_size' in config:
                self.spinMemory.setValue(config['memory_size'])

            if 'specify_count' in config:
                self.checkBoxSpecifyCount.setChecked(config['specify_count'])
                if config['specify_count']:
                    self.spinNumber.setDisabled(False)

            if 'buckets' in config:
                self.spinBucketNum.setValue(config['buckets'])

            if 'k' in config:
                select_k_combo(config['k'])

            if 'cmdline' in config:
                select_cmdline(config['cmdline'])

        self.comboSSD.currentIndexChanged.connect(self.update_form_items)
        self.comboCmdLine.currentIndexChanged.connect(self.update_form_items)
        self.comboHDD.currentIndexChanged.connect(self.update_tip_text)
        self.checkBoxNoBitfield.stateChanged.connect(self.check_nobitfield)

        self.comboCmdLine.currentIndexChanged.connect(self.slot_create_batch_tasks)
        self.comboSSD.currentIndexChanged.connect(self.slot_create_batch_tasks)
        self.comboHDD.currentIndexChanged.connect(self.slot_create_batch_tasks)
        self.checkBoxNoBitfield.stateChanged.connect(self.slot_create_batch_tasks)
        self.editFpk.textChanged.connect(self.slot_create_batch_tasks)
        self.editPpk.textChanged.connect(self.slot_create_batch_tasks)
        self.comboK.currentIndexChanged.connect(self.slot_create_batch_tasks)
        self.spinBucketNum.valueChanged.connect(self.slot_create_batch_tasks)
        self.spinReservedMemory.valueChanged.connect(self.slot_create_batch_tasks)

        self.update_form_items()
        self.slot_create_batch_tasks()
        self.update_tip_text()

    def slot_create_batch_tasks(self):
        self.batch_tasks.clear()
        self.treeWidgetTasks.clear()

        if self.comboSSD.currentData() != 'auto':
            self.buttonBox.button(self.buttonBox.Ok).setDisabled(False)
            return

        self.buttonBox.button(self.buttonBox.Ok).setDisabled(True)

        hdd_folder = self.comboHDD.currentData(Qt.UserRole)
        fpk = self.editFpk.toPlainText()
        ppk = self.editPpk.toPlainText()
        k = int(self.comboK.currentData(Qt.UserRole))
        cmdline = self.lineEditCmdLine.text()
        reserved_memory = self.spinReservedMemory.value()

        if not fpk or not ppk or not cmdline:
            return

        if cmdline == self.get_chia_plot_exe():
            QMessageBox.information(self, '提示', '使用多线程chia_plot.exe命令行不支持批量创建任务')
            return

        if hdd_folder != 'auto' and not os.path.exists(hdd_folder):
            QMessageBox.information(self, '提示', '最终目录不存在')
            return

        min_memory_size = 2 ** 30 * 3

        cpu_core = psutil.cpu_count()
        total_memory = psutil.virtual_memory().total
        available_memory = total_memory - reserved_memory * 1024 * 1024

        if available_memory < min_memory_size:
            QMessageBox.information(self, '提示', f'系统可使用的内存小于{size_to_str(min_memory_size)}，无法创建批量任务')
            return

        k_temp_size = get_k_temp_size(k)

        config = get_config()

        total_count = 0
        ssd_count_map = {}

        for ssd_folder in config['ssd_folders']:
            usage = get_disk_usage(ssd_folder)
            if not usage:
                continue
            count = int(usage.total // k_temp_size)
            total_count += count

            ssd_count_map[ssd_folder] = {
                'count': count,
                'reduced': 0,
            }

        if total_count == 0:
            QMessageBox.information(self, '提示', '当前系统资源无法创建任务')
            return

        def reduce_count():
            ssd_to_reduce = None
            last_ssd_reduce_count = 0
            for ssd in ssd_count_map:
                if ssd_count_map[ssd]['count'] == 0:
                    continue
                if ssd_to_reduce is None:
                    ssd_to_reduce = ssd_count_map[ssd]
                    last_ssd_reduce_count = ssd_to_reduce['reduced']
                if ssd_count_map[ssd]['reduced'] < last_ssd_reduce_count:
                    ssd_to_reduce = ssd_count_map[ssd]

            if ssd_to_reduce is None:
                return 0

            if ssd_to_reduce['count'] <= 0:
                return 0

            ssd_to_reduce['count'] -= 1
            ssd_to_reduce['reduced'] += 1

            return total_count - 1

        while available_memory // total_count < min_memory_size:
            total_count = reduce_count()
            if total_count == 0:
                break

        mem_per_task = available_memory // total_count
        thread_per_task = int(cpu_core / total_count + 2)
        if thread_per_task > cpu_core:
            thread_per_task = cpu_core

        if total_count == 0 or mem_per_task < min_memory_size:
            QMessageBox.information(self, '提示', '当前系统资源无法创建任务')
            return

        for ssd_folder in ssd_count_map:
            ssd = ssd_count_map[ssd_folder]
            count = ssd['count']

            if count > 6:
                max_hour = 8
            elif count == 5:
                max_hour = 7
            elif count == 4:
                max_hour = 6
            elif count == 3:
                max_hour = 5
            elif count <= 2:
                max_hour = 4
            else:
                max_hour = 8
            max_time = 60 * 60 * max_hour

            delay_per_task = int(max_time / count)

            for i in range(count):
                self.batch_tasks.append({
                    'ssd_folder': ssd_folder,
                    'hdd_folder': hdd_folder,
                    'memory': mem_per_task,
                    'thread': thread_per_task,
                    'delay': delay_per_task * i,
                })

        self.reload_batch_tasks(self.batch_tasks)

        if self.batch_tasks:
            self.buttonBox.button(self.buttonBox.Ok).setDisabled(False)

    def reload_batch_tasks(self, batch_tasks):
        self.treeWidgetTasks.clear()

        for task in batch_tasks:
            ssd_folder = task['ssd_folder']
            hdd_folder = task['hdd_folder']
            memory = task['memory']
            thread = task['thread']
            delay = task['delay']

            item = QTreeWidgetItem()

            index = 0

            item.setText(index, ssd_folder)

            index += 1
            if hdd_folder == 'auto':
                item.setText(index, '自动')
            else:
                item.setText(index, hdd_folder)

            index += 1
            item.setText(index, size_to_str(memory))

            index += 1
            item.setText(index, f'{thread}')

            index += 1
            item.setText(index, f'{seconds_to_str(delay)}')

            self.treeWidgetTasks.addTopLevelItem(item)

    def update_form_items(self):
        auto = self.comboSSD.currentData(Qt.UserRole) == 'auto'
        chia_plot = self.comboCmdLine.currentData(Qt.UserRole) == self.get_chia_plot_exe()

        self.checkBoxNoBitfield.setVisible(True)
        self.labelNoBitfield.setVisible(True)

        self.comboK.setVisible(True)
        self.labelK.setVisible(True)

        self.spinNumber.setVisible(True)
        self.checkBoxSpecifyCount.setVisible(True)

        self.labelTip.setVisible(not auto)
        self.treeWidgetTasks.setVisible(auto)

        self.spinMemory.setVisible(not auto)
        self.labelMemory.setVisible(not auto)

        self.spinThreadNum.setVisible(not auto)
        self.labelThreadNum.setVisible(not auto)

        self.timeEditDelay.setVisible(not auto)
        self.labelDelay.setVisible(not auto)

        self.spinReservedMemory.setVisible(auto)
        self.labelReserve.setVisible(auto)

        if auto:
            self.checkBoxSpecifyCount.setCheckState(0)
            self.checkBoxSpecifyCount.setVisible(False)
            self.spinNumber.setVisible(False)
            self.setWindowTitle('批量创建任务')
            self.buttonBox.button(self.buttonBox.Ok).setText('批量创建')
        else:
            self.checkBoxSpecifyCount.setVisible(True)
            self.spinNumber.setVisible(True)

            if not self.modify:
                self.setWindowTitle('创建任务')
                self.buttonBox.button(self.buttonBox.Ok).setText('创建')

            self.batch_tasks.clear()
            self.treeWidgetTasks.clear()

        if chia_plot:
            self.spinMemory.setVisible(False)
            self.labelMemory.setVisible(False)

            self.checkBoxNoBitfield.setVisible(False)
            self.labelNoBitfield.setVisible(False)

            self.comboK.setVisible(False)
            self.labelK.setVisible(False)

        self.adjustSize()
        self.update_tip_text()

    def update_tip_text(self):
        ssd_folder = self.comboSSD.currentData(Qt.UserRole)
        hdd_folder = self.comboHDD.currentData(Qt.UserRole)
        num = self.spinNumber.value()

        text = f'创建一条并发任务，使用固态硬盘{ssd_folder}作为临时目录，'
        if hdd_folder == 'auto':
            text += '向所有可用机械硬盘'
        else:
            text += f'向硬盘{hdd_folder} '

        if self.checkBoxSpecifyCount.isChecked():
            text += f'P{num}张图'
        else:
            text += f'P图，直到'
            if hdd_folder == 'auto':
                text += '所有硬盘填满为止'
            else:
                text += '硬盘填满为止'

        self.labelTip.setText(text)

        self.adjustSize()

    def get_builtin_exe(self):
        plat = platform.system()
        if plat == 'Windows':
            folder = 'windows'
        elif plat == 'Darwin':
            folder = 'macos'
        elif plat == 'Linux':
            folder = 'linux'
        else:
            return ''
        exe_cwd = os.path.join(BASE_DIR, 'bin', folder, 'plotter')
        if is_debug():
            return os.path.join(exe_cwd, 'test.exe')
        return os.path.join(exe_cwd, 'ProofOfSpace.exe')

    def get_chia_plot_exe(self):
        plat = platform.system()
        if plat == 'Windows':
            folder = 'windows'
        else:
            return ''
        exe_cwd = os.path.join(BASE_DIR, 'bin', folder, 'plotter')
        return os.path.join(exe_cwd, 'chia_plot.exe')

    def change_cmdline(self):
        data = self.comboCmdLine.currentData(Qt.UserRole)
        if data == 'select':
            chia_exe = QFileDialog.getOpenFileName(self, '选择钱包chia.exe', directory=os.getenv('LOCALAPPDATA'), filter='chia.exe')[0]
            self.lineEditCmdLine.setText(chia_exe)
        else:
            self.lineEditCmdLine.setText(data)

    def about_public_key(self):
        QMessageBox.information(self, '提示', '该软件不会向用户索要助记词。\n如果你已经安装了Chia官方钱包软件并且创建了钱包，fpk和ppk会自动获取。如果没有安装，请使用第三方工具（如：HPool提供的签名软件等）来生成。')

    def check_nobitfield(self, value):
        if value != 0:
            if QMessageBox.information(self, '提示', f'禁止位域会导致P图过程效率低且临时文件大，确定要禁止吗？',
                                       QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Cancel:
                self.checkBoxNoBitfield.setCheckState(0)

    def check_specify_count(self):
        self.spinNumber.setDisabled(not self.checkBoxSpecifyCount.isChecked())

        self.update_tip_text()

    def accept_modify(self):
        thread_num = self.spinThreadNum.value()
        memory_size = self.spinMemory.value()
        buckets = self.spinBucketNum.value()
        k = int(self.comboK.currentData(Qt.UserRole))
        nobitfield = self.checkBoxNoBitfield.isChecked()
        hdd_folder = self.comboHDD.currentData(Qt.UserRole)
        cmdline = self.lineEditCmdLine.text()

        if not cmdline:
            QMessageBox.information(self, '提示', '请选择程序')
            return

        if hdd_folder == 'auto':
            self.task.auto_hdd_folder = True
        else:
            self.task.auto_hdd_folder = False
            self.task.hdd_folder = hdd_folder

        self.task.number_of_thread = thread_num
        self.task.memory_size = memory_size
        self.task.buckets = buckets
        self.task.k = k
        self.task.nobitfield = nobitfield
        self.task.cmdline = cmdline

        if cmdline == self.get_builtin_exe():
            self.task.plotter_type = PLOTTER_BUILTIN
        elif cmdline == get_official_chia_exe():
            self.task.plotter_type = PLOTTER_OFFICIAL
        elif cmdline == self.get_chia_plot_exe():
            self.task.plotter_type = PLOTTER_CHIA_PLOT

        if self.task.specify_count:
            for sub in self.task.sub_tasks:
                if not sub.finish and not sub.working:
                    if hdd_folder == 'auto':
                        sub.hdd_folder = ''
                    else:
                        sub.hdd_folder = hdd_folder

                    sub.buckets = buckets
                    sub.k = k
                    sub.nobitfield = nobitfield

        super().accept()
        return

    def accept(self) -> None:
        if self.modify:
            self.accept_modify()
            return

        fpk = self.editFpk.toPlainText()
        ppk = self.editPpk.toPlainText()
        buckets = self.spinBucketNum.value()
        k = int(self.comboK.currentData(Qt.UserRole))
        nobitfield = self.checkBoxNoBitfield.isChecked()
        cmdline = self.lineEditCmdLine.text()

        ssd_folder = self.comboSSD.currentData()
        hdd_folder = self.comboHDD.currentData()

        CreatePlotDialog.last_ssd_folder = ssd_folder
        CreatePlotDialog.last_hdd_folder = hdd_folder

        delayTime = self.timeEditDelay.time()
        delay = delayTime.hour() * 60*60 + delayTime.minute() * 60 + delayTime.second()

        specify_count = self.checkBoxSpecifyCount.isChecked()
        number = self.spinNumber.value()
        thread_num = self.spinThreadNum.value()
        memory_size = self.spinMemory.value()

        if not cmdline:
            QMessageBox.information(self, '提示', '请选择命令行程序')
            return

        if ssd_folder != 'auto' and not os.path.exists(ssd_folder):
            QMessageBox.information(self, '提示', '临时目录不存在')
            return

        if hdd_folder != 'auto' and not os.path.exists(hdd_folder):
            QMessageBox.information(self, '提示', '最终目录不存在')
            return

        if not fpk:
            QMessageBox.information(self, '提示', '请输入fpk')
            return

        if not ppk:
            QMessageBox.information(self, '提示', '请输入ppk')
            return

        if fpk.startswith('0x'):
            fpk = fpk[2:]
        if ppk.startswith('0x'):
            ppk = ppk[2:]

        if len(fpk) != 96:
            QMessageBox.information(self, '提示', 'fpk格式错误，请检查')
            return
        if len(ppk) != 96:
            QMessageBox.information(self, '提示', 'ppk格式错误，请检查')
            return

        if not specify_count:
            number = 1

        if ssd_folder == 'auto' and not self.batch_tasks:
            QMessageBox.information(self, '提示', f'当前系统资源无法创建批量任务')
            return

        if hdd_folder != 'auto':
            hdd_usage = get_disk_usage(hdd_folder)

            if hdd_usage is None:
                QMessageBox.information(self, '提示', f'目录{hdd_folder}无法使用')
                return

            k_size = get_k_size(k)
            if not is_debug() and hdd_usage.free < k_size:
                if QMessageBox.information(self, '提示', f'最终目录的空间不足{size_to_str(k_size)}，确定要继续吗？', QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Cancel:
                    return

        config = get_config()

        config['cmdline'] = cmdline
        config['fpk'] = fpk
        config['ppk'] = ppk
        config['buckets'] = buckets
        config['k'] = k
        config['specify_count'] = specify_count
        config['num'] = number
        config['thread_num'] = thread_num
        config['memory_size'] = memory_size

        save_config()

        self.result.clear()
        if ssd_folder == 'auto':
            for batch_task in self.batch_tasks:
                _ssd_folder = batch_task['ssd_folder']
                _hdd_folder = batch_task['hdd_folder']
                _memory = batch_task['memory']
                _thread = batch_task['thread']
                _delay = batch_task['delay']

                _memory = _memory // 1024 // 1024

                task = self.create_task(cmdline=cmdline, fpk=fpk, ppk=ppk, buckets=buckets, k=k, nobitfield=nobitfield,
                                        ssd_folder=_ssd_folder, hdd_folder=_hdd_folder, specify_count=False,
                                        count=1, thread_num=_thread, memory_size=_memory, delay=_delay)
                if task:
                    self.result.append(task)
        else:
            task = self.create_task(cmdline=cmdline, fpk=fpk, ppk=ppk, buckets=buckets, k=k, nobitfield=nobitfield,
                                    ssd_folder=ssd_folder, hdd_folder=hdd_folder, specify_count=specify_count,
                                    count=number, thread_num=thread_num, memory_size=memory_size, delay=delay)
            if task:
                self.result = [task]

        if not self.result:
            return

        super().accept()

    def create_task(self, cmdline, fpk, ppk, buckets, k, nobitfield, ssd_folder, hdd_folder, specify_count, count,
                    thread_num, memory_size, delay) -> Optional[PlotTask]:
        temporary_folder = os.path.join(ssd_folder, make_name(12))
        temporary_folder = temporary_folder.replace('\\', '/')

        try:
            os.mkdir(temporary_folder)
        except:
            QMessageBox.information(self, '提示', '创建临时目录失败 %s' % temporary_folder)
            return None

        task = PlotTask()

        task.cmdline = cmdline
        if cmdline == self.get_builtin_exe():
            task.plotter_type = PLOTTER_BUILTIN
        elif cmdline == get_official_chia_exe():
            task.plotter_type = PLOTTER_OFFICIAL
        elif cmdline == self.get_chia_plot_exe():
            task.plotter_type = PLOTTER_CHIA_PLOT

        task.create_time = datetime.now()
        task.fpk = fpk
        task.ppk = ppk
        task.buckets = buckets
        task.k = k
        task.nobitfield = nobitfield
        task.ssd_folder = ssd_folder
        if hdd_folder == 'auto':
            task.auto_hdd_folder = True
        else:
            task.auto_hdd_folder = False
            task.hdd_folder = hdd_folder
        task.temporary_folder = temporary_folder
        task.specify_count = specify_count
        task.count = count
        task.number_of_thread = thread_num
        task.memory_size = memory_size
        task.delay_seconds = delay

        if specify_count:
            for i in range(count):
                task.sub_tasks.append(PlotSubTask(task, i))
        else:
            task.sub_tasks.append(PlotSubTask(task, 0))

        return task
