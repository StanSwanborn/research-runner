class ScreenProcedure:
    @staticmethod
    def pyautogui_position_fix_and_center(pos):
        fixed = ScreenProcedure._macOS_position_fix(pos)
        return ScreenProcedure._macOS_position_center(fixed)

    @staticmethod
    def pyautogui_position_fix(pos):
        return ScreenProcedure._macOS_position_fix(pos)

    @staticmethod
    def pyautogui_position_center(pos):
        return ScreenProcedure._macOS_position_center(pos)

    @staticmethod
    def _macOS_position_fix(pos):
        return (pos[0] / 2, pos[1] / 2, pos[2] / 2, pos[3] / 2) # Macbook screen bug workaround

    @staticmethod
    def _macOS_position_center(pos: (int, int, int, int)):
        return (pos[0] + (pos[2] / 2), 
                pos[1] + (pos[3] / 2),
                pos[2],
                pos[3])