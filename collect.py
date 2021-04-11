import sys
from copy_plugin import RunTicket

if __name__ == '__main__':
    if sys.argv[1] != 'right' and sys.argv[1] != 'left':
        print('parameter is wrong! please input right or left')
    if len(sys.argv) >= 3:
        run_collect = RunTicket(sys.argv[2])
    else:
        run_collect = RunTicket()
    run_collect.setup(None)
    run_collect.clear_all_fight(sys.argv[1], 0)  # 0 is mean run forever
