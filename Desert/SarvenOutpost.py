#http://codecombat.com/play/level/sarven-outpost
# Ogres are attacking a nearby outpost!
# Command the hero to defend the tiny settlement.
# Time your patrol with a watch so no ogres can get through.
def attack(target):
    if target:
        if(self.isReady("bash")):
            self.bash(target)
        elif(self.isReady("power-up")):
            self.powerUp()
            self.attack(target)
        elif(self.isReady("cleave")):
            self.cleave(target)
        elif(self.canCast('chain-lightning', target)):
            self.cast('chain-lightning', target)
        else:
            self.shield()

while True:
    polarPos = hero.now() / 4
    xPos = 40 + Math.cos(polarPos) * 20 # Number between 20 and 60.
    yPos = 34 + Math.sin(polarPos) * 20 # Number between 14 and 54.
    hero.moveXY(xPos, yPos)
    # Check for ogres and defeat them!
    # Make sure to attack the ogres while their health is above 0.
    enemy = self.findNearest(self.findEnemies())
    while enemy:
        attack(enemy)
        enemy = self.findNearest(self.findEnemies())
