

class Packet:
    def __init__(self, hex_input):
        self.binary_input = self.convert_to_binary(hex_input)
        self.version = self.binary_input[:3]
        self.packet_type_id = self.binary_input[3:6]
        self.length_type_id = self.binary_input[6]
        self.payload = "bits"
        print(f"\nHex: {hex_input}\nBin: {self.binary_input}\nVer: {self.version}\nPacket Type: {self.packet_type_id}\nLength Type: {self.length_type_id}\nPayload: {self.payload}")

    @staticmethod
    def convert_to_binary(hex_input) -> str:
        bin = []
        for char in hex_input:
            bin += "{0:04b}".format(int(char, 16))
        return "".join(bin)

    def __repr__(self):
        return f"Packet - version: {self.version}, packet type: {self.packet_type_id}, length type: {self.length_type_id}"



def main():
    with open("testinput.txt") as file:
        raw_input = file.read().strip()

    packet = Packet(raw_input)
    # print(packet)



if __name__ == "__main__":
    main()