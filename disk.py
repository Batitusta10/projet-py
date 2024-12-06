class Disk:
    def __init__(self, total, used):
        self.__total = total
        self.__used = used

    @property
    def free(self):
        return self.__total - self.__used

    @property
    def used_perc(self):
        return self.__used / self.__total

    def __str__(self):
        return f"Disk[total: {self.__total} Gb, used: {self.__used} Gb]"

    def __lt__(self, other):
        return self.used_perc < other.used_perc

    def __eq__(self, other):
        return self.used_perc == other.used_perc

    def __gt__(self, other):
        return self.used_perc > other.used_perc

    def __le__(self, other):
        return self.used_perc <= other.used_perc

    def __ge__(self, other):
        return self.used_perc >= other.used_perc

    def __ne__(self, other):
        return self.used_perc != other.used_perc
    
if __name__ == '__main__':
    disk1 = Disk(total = 10, used = 2)
    disk2 = Disk(total = 20, used = 5)
    print(disk1.free) # 8
    print(disk2.free) # 15
    print(disk1.used_perc) # 0.2
    print(disk2.used_perc) # 0.25
    disks = [disk1, disk2]
    disks_sorted = sorted(disks) # trié selon le pourcentage
    print(disks_sorted) # [Disk[total: 10 Gb, used: 2 Gb], Disk[total: 20 Gb, used: 5 Gb]]