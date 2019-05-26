# 工厂方法模式
from abc import ABCMeta,abstractmethod
class Sender(metaclass=ABCMeta):
    @abstractmethod
    def auto_send(self):
        pass


class SmsSender(Sender):
    def auto_send(self):
        print('i am sms sender')


class MailSender(Sender):
    def auto_send(self):
        print('i am mail sender')


class SenderFactory:
    @staticmethod
    def produceSms():
        return SmsSender()
    
    @staticmethod
    def produceMail():
        return MailSender()




if __name__ == "__main__":
    factory = SenderFactory()
    sms = factory.produceSms()
    sms.auto_send()