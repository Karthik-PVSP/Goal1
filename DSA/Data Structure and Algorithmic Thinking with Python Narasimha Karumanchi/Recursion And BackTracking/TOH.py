numberOfDisks=int(input("Please enter the number of disks to move"))
#in this game we have 3 towers we need to move rings from one tower to final destination using auxilary tower.
def TOI(disk:int,fromTower,toTower,auxTower):
    if disk:
        #move top n-1 disks from source to aux tower
        TOI(disk-1,fromTower,auxTower,toTower)
        print(f"Move the disk{disk},from {fromTower} to {toTower}")
        TOI(disk-1,auxTower,toTower,fromTower)
TOI(numberOfDisks,"a","c","b")