class TeamMember():
    def __init__(self, name):
        self.name = name
        print(f'{name} joins to the team')

    def go_to_kitchen(self):
        print(f'{self.name} I ned coffee')
    def complain(self):
        print(f'{self.name} This app looks not nice')

class Tester(TeamMember):
    def __init__(self, name, break_impact):
        TeamMember.__init__(self, name)
        self.break_impact = break_impact
    def hi_complain(self):
        super().complain()
        print(f'{self.name}: I\'ve never seen such poor coded app')
    def test(self):
        print(f'{self.name}: Testing, What\'s here.. hmmm')

class Developer(TeamMember):
    def __init__(self, name, prog_langueage):
        TeamMember.__init__(self, name)
        self.prog_language = prog_langueage
    def write_code(self):
        print(f'{self.name}: Coding fix coding')
    def make_bug(self):
        print(f'{self.name}: Coding bug coding')

class Leader(TeamMember):
    def __init__(self, name, daily_meetings):
        TeamMember.__init__(self, name)
        self.daily_meetings = daily_meetings
    def make_meeting(self):
        print(f'{self.name}: We here to talk')
    def prise(self):
        print(f'{self.name}: Good team - app is awsome')

class Automation(Tester):
    def __init__(self, name, break_impact, will_autmoate_all):
        Tester.__init__(self, name, break_impact)
        self.will_automate_all = will_autmoate_all
    def auto_click(self):
        print(f'{self.name}: Selenium clicking')
    def fix_own_code(self):
        print(f'{self.name} Testers bug is not a bug')
class Performance(Tester):
    def __init__(self, name, break_impact, voodoo_skill_level):
        Tester.__init__(self, name, break_impact)
        self.voodoo_skill_level = voodoo_skill_level
    def very_hi_complain(self):
        super().hi_complain()
        print(f'{self.name}: This is total mess')
    def one_test_break_all(self):
        print(f'{self.name}: Open page 1 million times in 2 seconds')

print('\nTeam forming')
senior_bart = Developer('Bartosz', 'Java')
junior_remi = Tester('Remigiusz', 3)
medium_kacha = Automation('Katarzyna', 6, True)
senior_gocha = Performance('Małgorzata', 9, 100)
cheef_mark = Leader('Marek', 3)

print('\nStart project')
cheef_mark.make_meeting()
senior_bart.write_code()
junior_remi.test()

print('\nDevelopment')
senior_bart.write_code()
senior_bart.make_bug()
medium_kacha.auto_click()
medium_kacha.hi_complain()

print('\nProduction testing')
senior_gocha.test()
senior_gocha.hi_complain()
senior_gocha.one_test_break_all()
senior_gocha.very_hi_complain()
junior_remi.hi_complain()
senior_bart.complain()

print('\nLeader reaction')
cheef_mark.make_meeting()
cheef_mark.complain()
senior_bart.write_code()
junior_remi.test()
cheef_mark.prise()

print('\nTeam leaves work')
senior_bart.go_to_kitchen()
junior_remi.go_to_kitchen()
medium_kacha.go_to_kitchen()
senior_gocha.go_to_kitchen()
