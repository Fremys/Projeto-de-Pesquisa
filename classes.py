class PontoOnibus:
    # método construtor
    def __init__(self, id, id_ponto, cod_linha, nome_linha, nome_sublinha, origem, ident_ponto, geo):
        self.id = id
        self.id_ponto = id_ponto
        self.cod_linha = cod_linha
        self.nome_linha = nome_linha
        self.nome_sublinha = nome_sublinha
        self.origem = origem
        self.ident_ponto = ident_ponto
        self.geo = geo
    
    #GETS 
    def getId(self):
        return self.id
    
    def getIdPonto(self):
        return self.id_ponto
    
    def getCodLinha(self):
        return self.cod_linha
    
    def getNomeLinha(self):
        return self.nome_linha
    
    def getNomeSubLinha(self):
        return self.nome_sublinha
    
    def getOrigem(self):
        return self.origem
    
    def getIdenPonto(self):
        return self.ident_ponto
    
    def getGeo(self):
        return self.geo
    
    #SETS
    def setId(self, id):
        self.id = id
        
    def setIdPonto(self, idPonto):
        self.id_ponto = idPonto
        
    def setCodLinha(self, codLinha):
       self.cod_linha = codLinha
       
    def setNomeLinha(self, nomeLinha):
        self.nome_linha = nomeLinha
        
    def setNomeSubLinha(self, subLinha):
        self.sub_linha = subLinha
    
    def setOrigem(self, origem):
        self.origem = origem
    
    def setIdentPonto(self, identPonto):
        self.ident_ponto = identPonto
        
    def setGeo(self, geo):
        self.geo = geo
        
    