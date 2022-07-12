import json
from abc import ABC, abstractmethod


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, file_name, data):
        pass


class SerialToJson(SerializationInterface):
    def serialize(self, file_name, data_json):
        with open(file_name, 'w', encoding='utf-8') as fh:
            json.dump(data_json, fh)

    def deserialize(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as fh:
            return json.load(fh)


class SerialToBin(SerializationInterface):
    def serialize(self, file_name, data):
        with open(file_name, 'wb') as fh:
            fh.write(data.encode())

    def deserialize(self, file_name):
        with open(file_name, 'rb') as fh:
            return fh.read().decode()





data_test = 'Python Web 6'

instance_bin = SerialToBin()
instance_json = SerialToJson()


instance_bin.serialize('test.bin', data_test)
instance_json.serialize('test.json', data_test)

print(instance_bin.deserialize('test.bin'))
print(instance_json.deserialize('test.json'))