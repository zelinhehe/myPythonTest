# @Time    : 2019/6/12 4:40 PM
# @Author  : Wu Kun
# @Email   : bewithyou@126.com


class Computer:
    def __init__(self, serial_num):
        self.serial_num = serial_num
        self.memory = None

    def __str__(self):
        return 'Memory: {}GB'.format(self.memory)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG1')

    def configure_memory(self, amount):
        self.computer.memory = amount


class Engineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    enginner = Engineer()
    enginner.construct_computer(8)
    computer = enginner.computer
    print(computer)
