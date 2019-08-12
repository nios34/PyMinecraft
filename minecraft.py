from srcds.rcon import RconConnection
import json

class Automation:
    def __init__(self, Minecraft_class):
        self.Mc = Minecraft_class
        self.Machines = {}
        pass

    def Create_machine(self):
        # Wait for update...
        pass
    pass

class Create:
    def __init__(self, Minecraft_class):
        self.Mc = Minecraft_class
        pass

    def Rut_singe(self, where, block, TN=0, NBT={}):
        self.Mc.execute('setblock %s %s %s %s %s %s' % (
            where[0], where[1], where[2], block, TN, json.dumps(NBT)))
        pass

    def Put(self, where1, where2, block, TN=0, NBT={}):
        if where2[0][0] == '~' and where2[1][0] == '~' and where2[2][0] == '~':
            where2[0] = where2[0].replace('~', '')
            where2[1] = where2[1].replace('~', '')
            where2[2] = where2[2].replace('~', '')
            where2[0] = int(where2[0])
            where2[1] = int(where2[1])
            where2[2] = int(where2[2])
            self.Mc.execute('fill %s %s %s %s %s %s %s %s %s' % (
                where1[0], where1[1], where1[2], where1[0] + where2[0], where1[1] + where2[1], where1[2] + where2[2], block, TN, json.dumps(NBT)))
        else:
            self.Mc.execute('fill %s %s %s %s %s %s %s %s %s' % (
                where1[0], where1[1], where1[2], where2[0], where2[1], where2[2], block, TN, json.dumps(NBT)))
            pass
        pass
    pass


class Mana:
    def __init__(self, Minecraft_class):
        self.Mc = Minecraft_class
        pass

    def Mode(self, mode='0', Name='@a'):
        self.Mc.execute('gamemode %s %s' % (mode, Name))
        pass

    def Give_OP(self, Name):
        self.Mc.execute('op %s' % Name)
        pass

    def Revoke_OP(self, Name):
        self.Mc.execute('deop %s' % Name)
        pass

    def Ban(self, Name):
        self.Mc.execute('ban %s' % Name)
        pass

    def Kill(self, Name):
        self.Mc.execute('kill %s' % Name)
        pass

    def Kill_all_player(self):
        self.Kill('@a')
        pass

    def Kill_all_object(self):
        self.Kill('@e')
        pass

    def Clean_item(self):
        self.Kill('@e[type=Item]')
        pass

    def Set_weather(self, wt):
        self.Mc.execute('weather %s' % wt)
        pass
    pass


class Minecraft:
    def __init__(self, IP='localhost'):
        self.Host = IP
        pass

    def driver(self, long=20, char='-'):
        self.print_raw({"text": char*long})
        pass

    def execute(self, Command):
        Connection = RconConnection(
            self.Host, single_packet_mode=True, port=25575, password='Minecraft')
        Connection.exec_command('%s' % Command)
        pass

    def print_refer_url(self, Content, Refer_to="http://localhost", player="@a", color='white', underlined=False, bold=False, italic=False,  strikethrough=False,  obfuscated=False):
        Data = {"text": Content, "color": color, "underlined": underlined, "bold": bold,
                "italic": italic, "strikethrough": strikethrough, "obfuscated": obfuscated, "clickEvent": {"action": "open_url", "value": Refer_to}}
        pass

    def print_run_cmd(self, Content, Cmd, player="@a", color='white', underlined=False, bold=False, italic=False,  strikethrough=False,  obfuscated=False):
        Data = {"text": Content, "color": color, "underlined": underlined, "bold": bold,
                "italic": italic, "strikethrough": strikethrough, "obfuscated": obfuscated, "clickEvent": {"action": "run_command", "value": Cmd}}
        pass

    def print(self, Content, player="@a", color='white', underlined=False, bold=False, italic=False,  strikethrough=False,  obfuscated=False):
        Data = {"text": Content, "color": color, "underlined": underlined, "bold": bold,
                "italic": italic, "strikethrough": strikethrough, "obfuscated": obfuscated}
        self.print_raw(Data, player)
        pass

    def print_raw(self, Content_raw, player='@a'):
        Content_json = json.dumps(Content_raw)
        self.execute('tellraw %s %s' % (player, Content_json))
        pass
    pass
