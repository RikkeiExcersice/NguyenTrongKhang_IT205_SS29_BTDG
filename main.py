from abc import ABC, abstractmethod
class BaseCharacter(ABC):
    def __init__(self, base_hp):
        self.__base_hp = base_hp

    @property
    def base_hp(self):
        return self.__base_hp

    @abstractmethod
    def attack_enemy(self):
        pass

    def __add__(self, other):
        return self.base_hp + other.base_hp
    
class MagicalStance:
    def attack_enemy(self):
        return 150.0

class Warrior(BaseCharacter):
    def __init__(self, base_hp, strength):
        super().__init__(base_hp)
        self.strength = strength

    def attack_enemy(self):
        return self.strength * 2.5


class Spellblade(Warrior, MagicalStance):
    def __init__(self, base_hp, strength):
        super().__init__(base_hp, strength)

    def attack_enemy(self):
        physical_damage = Warrior.attack_enemy(self)
        magic_damage = MagicalStance.attack_enemy(self)
        return physical_damage + magic_damage


class VolcanoZone:
    def activate_buff(self, character):
        character.strength += 20
        print("Sức mạnh +20")
        print("Sức mạnh hiện tại:", character.strength)


def apply_battleground_effect(environment, character):
    environment.activate_buff(character)

current_hero = None

current_hero = None

while True:
    print("-" * 50)
    print("════ RPG GAME CORE MENU ════")
    print("=" * 55)
    print("1. Khởi tạo Ma Kiếm sĩ Spellblade & Xem cấu trúc MRO")
    print("2. Ra lệnh tấn công & Kích hoạt chiến trường (Duck Typing)")
    print("0. Thoát")
    print("-" * 50)

    choice = input("Chọn chức năng (0-2): ")

    match choice:
        case "1":
            print("\n--- KHỞI TẠO MA KIẾM SĨ SPELLBLADE ---")
            hp = int(input("Nhập lượng máu cơ bản (HP): "))
            strength = int(input("Nhập chỉ số sức mạnh (Strength): "))
            current_hero = Spellblade(hp, strength)
            print("\n[Thành công]: Khởi tạo nhân vật Spellblade thành công!")

            print("\n[MRO Architecture]: ", end="")
            print(" -> ".join(cls.__name__ for cls in Spellblade.__mro__))
            print(f"\n[Overloading __add__]: Tổng HP tích lũy khi gộp đội hình: {current_hero + current_hero}")
        
        case "2":
            print("\n--- THI THIẾT KẾ GIAO TRANH & DUCK TYPING ---")
            if current_hero is None:
                print("Chưa có kiếm sĩ")
            else:
                damage = current_hero.attack_enemy()
                print(f"[Đa hình] Spellblade vung kiếm ma thuật gây tổng sát thương: {damage} DMG")
                zone = VolcanoZone()
                print("[Duck Typing]: Xác thực môi trường trận đấu thành công!")
                apply_battleground_effect(zone, current_hero)

        case "0":
            print("Đã thoát chương trình !!!")
            break
        
        case _:
            print("Lựa chọn không hợp lệ")