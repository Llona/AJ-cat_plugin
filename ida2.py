from time import sleep
from copy_plugin import RunTicket


class Ida2Go(RunTicket):
    def __init__(self):
        super(Ida2Go, self).__init__()
        # super(RunTicket, self).__init__()
        self.fight_type = 'joker'

        self.setup(None)
        self.run()

    def clear_fighting(self, is_run_copy=True):
        if self.fight_type == 'joker':
            self.touch_pos(self.fight_role2_pos)
            sleep(0.3)
            self.touch_pos(self.fight_skill_change)
            sleep(0.3)
            self.touch_pos(self.fight_role5_pos)
            sleep(0.3)
        else:
            self.touch_pos(self.any2_pos)
            sleep(0.3)

        self.touch_pos(self.attack)
        sleep(5)
        self.touch_pos(self.any_pos)

    def run(self):
        self.clear_all_fight('left', 0)


if __name__ == '__main__':
    run = Ida2Go()
    # run.run()
