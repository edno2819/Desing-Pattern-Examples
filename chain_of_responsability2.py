class HandlerChainOfResponsability:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)
        if self._successor:
            return self._successor.handle_request(handled)
        return handled

    def _handle(self, request):
        raise NotImplementedError(
            'Este método deve ser implementado pelas subclasses')


class ParseType1(HandlerChainOfResponsability):
    def _handle(self, request):
        if request.find("casa")!=-1:
            print('Parse Nível 1: Resolvi a solicitação.')
            return request.replace("casa", "mansão")
        return request


class ParseType2(HandlerChainOfResponsability):
    def _handle(self, request):
        if request.find("_")!=-1:
            print('Parse Nível 2: Resolvi a solicitação.')
            return request.replace("_", " ")
        return request


class ParseType3(HandlerChainOfResponsability):
    def _handle(self, request):
        print('Parse Nível 3: Resolvi a solicitação.')
        return request.replace("#", "").replace("&", "").replace("/", " ")

class ParseTypeDefault(HandlerChainOfResponsability):
    def _handle(self, request):
        return request.strip() + "."



# Configurando a cadeia de responsabilidade
support_chain = ParseType1(ParseType2(ParseType3(ParseTypeDefault())))

# Solicitando suporte
result = support_chain.handle_request(' casa/teto/vidro ')
print(result)