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
    def __init__(self, name, hp, power, mp, magic_power):
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        super().__init__(name, hp, power)

    def magic_attack(self, other):
        self.mp -= 2
        damage = random.randint(self.magic_power - 2, self.magic_power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


def create_player():
    print("플레이어 생성")
    return Player(input("플레이어 이름:"), 100, 10, 10, 20)


def create_monster():
    print("몬스터 생성")
    return Monster("슬라임", 100, 10)


player = create_player()
monster = create_monster()
turns = 0


while (True):
    turns += 1
    print(f"[{turns}턴] 플레이어 체력:{player.hp}/{player.max_hp} 마나:{player.mp}/{player.max_mp} / 몬스터 체력:{monster.hp}/{monster.max_hp}")

    print("<당신의 차례>")
    act = int(input("당신의 행동 (1.일반공격 2.마법공격):"))
    if act == 1:
        player.attack(monster)
    elif act == 2:
        player.magic_attack(monster)

    if monster.hp == 0:
        print("당신이 이겼습니다.")
        break

    print("<상대의 차례>")
    monster.attack(player)
    if player.hp == 0:
        print("상대가 이겼습니다.")
        break

    player.show_status()
    monster.show_status()
    print("턴종료\n")

print("게임 종료")
