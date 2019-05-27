# 建造者模式
#
class SmsSender:
    def auto_send(self):
        print('i am sms sender')


class MailSender:
    def auto_send(self):
        print('i am mail sender')



class Builder:
    product = {}
    product.setdefault('sms',[])
    product.setdefault('mail',[])

    def produce_sms(self,count):
        for _ in range(count):
            self.product['sms'].append(SmsSender())
    
    def procude_mail(self,count):
        for _ in range(count):
            self.product['mail'].append(MailSender())

if __name__ == "__main__":
    builder = Builder()
    builder.produce_sms(10)
    builder.procude_mail(10)
    print(builder.product)