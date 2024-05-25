class HandlerChainOfResponsability:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)
        if not handled and self._successor:
            return self._successor.handle_request(request)
        return handled

    def _handle(self, request):
        raise NotImplementedError(
            'Este método deve ser implementado pelas subclasses')


class ParseType1(HandlerChainOfResponsability):
    def _handle(self, request):
        if request.find("/")!=-1:
            print('Parse Nível 1: Resolvi a solicitação.')
            return request.split("/") 
        return False


class ParseType2(HandlerChainOfResponsability):
    def _handle(self, request):
        if request.find("_")!=-1:
            print('Parse Nível 2: Resolvi a solicitação.')
            return request.split("_") 
        return False


class ParseType3(HandlerChainOfResponsability):
    def _handle(self, request):
        if request.find("%")!=-1:
            print('Parse Nível 3: Resolvi a solicitação.')
            return request.split("%") 
        return False

class ParseTypeDefault(HandlerChainOfResponsability):
    def _handle(self, request):
        return request.split(" ") 



# Configurando a cadeia de responsabilidade
support_chain = ParseType1(ParseType2(ParseType3(ParseTypeDefault())))

# Solicitando suporte
result = support_chain.handle_request('casa/teto/vidro')
result = support_chain.handle_request('casa_teto_vidro')
result = support_chain.handle_request('casa%teto%vidro')
result = support_chain.handle_request('Nível 4')