# 抽象工厂模式

class Sender(object):
    def auto_send(self):
        pass


class SmsSender(Sender):
    def auto_send(self):
        print('i am sms sender')


class MailSender(Sender):
    def auto_send(self):
        print('i am mail sender')


class SenderProduce(object):
    def produce(self):pass


class SendMailFactory(SenderProduce):
    def produce(self):
        return MailSender()


class SendSmsFactory(SenderProduce):
    def produce(self):
        return SmsSender()


if __name__ == "__main__":
    factory = SendMailFactory()
    sender = factory.produce()
    sender.auto_send()
