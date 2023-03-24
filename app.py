import random


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


def create_player():
    print("플레이어 생성")
    return Player(input("플레이어 이름:"), 10, 10)


def create_monster():
    print("몬스터 생성")
    return Monster("슬라임", 10, 10)


player = create_player()
monster = create_monster()
turns = 0


while (True):
    turns += 1
    print(f"[{turns}턴] 플레이어 체력:{player.hp}/{player.max_hp} 몬스터 체력:{monster.hp}/{monster.max_hp}")

    if turns == 3:
        break
