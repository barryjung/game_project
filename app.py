import random
import time


class Character:
    # 모든 캐릭터의 모체가 되는 클래스

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

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


def create_player():
    return Player(input("결투장에 올라서는 (플레이어 이름):"), 100, 10, 10, 20)


def create_monster():
    monster_doc = [
        ["슬라임", 50, 10],
        ["고블린", 100, 10],
        ["오우거", 150, 10]
    ]
    monster_select = random.randint(1, 3)
    name = monster_doc[monster_select][0]
    hp = monster_doc[monster_select][1]
    power = monster_doc[monster_select][2]
    print(f"그 상대는 {name}!\n")
    return Monster(name, hp, power)


# 시작부분
print("게임 시작")
player = create_player()
monster = create_monster()
turns = 0
time.sleep(1)


# 게임진행
while (True):
    turns += 1
    print(f"[{turns}턴]")
    player.show_status()
    monster.show_status()

    print("<당신의 차례>")
    act_select = int(input("당신의 행동 1.일반공격 2.마법공격(mp 2소모):"))
    if act_select == 1:
        player.attack(monster)
    elif act_select == 2:
        player.magic_attack(monster)

    if monster.hp == 0:
        print("당신이 이겼습니다.")
        break

    print("<상대의 차례>")
    monster.attack(player)
    if player.hp == 0:
        print("상대가 이겼습니다.")
        break

    print(f"[{turns}턴종료]\n")
    time.sleep(1)


# 끝부분
print("게임 종료")
