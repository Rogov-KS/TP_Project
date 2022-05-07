from army import Army
import configuration as config
from fortresses import Fortress

class Fight:
    specialization = {'horse': 'swordsmen', 'swordsmen': 'pikemen', 'pikemen': 'horse'}
    antispecialization = {'horse': ['pikemen', 'horse', 'swordsmen'], 'swordsmen': ['horse', 'swordsmen', 'pikemen'], 'pikemen': ['swordsmen', 'pikemen', 'horse']}

    def fortress_fight(self, army_1: Army, fort: Fortress):
        for cur_type in self.antispecialization[army_1.type]:
            cur_army = Army(0, 0, fort.army[cur_type], fort.color, cur_type, fort.num_)
            while cur_army.num_ > 0 and army_1.num_ > 0:
                self.process_of_fight(army_1, cur_army)

            fort.army[cur_type] = cur_army.num_
            cur_army.kill()

        if army_1.num_ == 0:
            army_1.kill()
        else:
            # castle has been skjgb
            fort.color = army_1.color
            fort.army[army_1.type] = army_1.num_
            print("WIN")


    def accept_friend_army(self, army: Army, fort: Fortress):
        fort.army[army.type] += army.num()
        army.kill()

    def army_fight(self, army_1: Army, army_2: Army):
        self.process_of_fight(army_1, army_2)
        self.look_for_survivors(army_1)
        self.look_for_survivors(army_2)

    def process_of_fight(self, army_1: Army, army_2: Army):
        damage_to_1 = army_2.num_
        if army_1.type == self.specialization[army_2.type]:
            damage_to_1 *= config.damage_bonus
        damage_to_2 = army_1.num_
        if army_2.type == self.specialization[army_1.type]:
            damage_to_2 *= config.damage_bonus
        army_1.num_ -= damage_to_1
        army_1.num_ = max(0, army_1.num_)
        army_2.num_ -= damage_to_2
        army_2.num_ = max(0, army_2.num_)

    def look_for_survivors(self, army_1: Army):
        if army_1.num_ <= 0:
            army_1.kill()
