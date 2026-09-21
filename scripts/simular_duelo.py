import random, statistics, itertools
R=random.randint
def d(n,f): return sum(R(1,f) for _ in range(n))
def d20(): return R(1,20)
def atk(bonus, df, adv=False):
    r=d20()
    if adv: r=max(r,d20())
    return r, (r!=1 and (r==20 or r+bonus>=df))

class ET:   # Inato + Esp. em Tecnica
    nome="Tecnico"
    def __init__(s): s.pv=33; s.pe=29; s.df=16; s.init=7; s.rr=True; s.refl=4; s.fort=4; s.desprev=0
    def defesa(s): return s.df-(3 if s.desprev>0 else 0)
    def turno(s, o):
        if s.pe>=6:          # Olhos da Morte concentrado + Feitico Preciso
            s.pe-=6; r,h=atk(13,o.defesa())
            if h: o.dano(d(8,8)+5+(d(8,8) if r==20 else 0))
        else:                # duas pistolas (INT pela Tecnica de Combate)
            r,h=atk(9,o.defesa())
            if h: o.dano(d(1,10)+5)
            r,h=atk(9,o.defesa())
            if h: o.dano(d(1,10))
    def dano(s,x):
        if s.pe>=4 and x>=12: s.pe-=4; x=max(0,x-16)   # Cobrir-se
        s.pv-=x
    def fim(s):
        if s.desprev>0: s.desprev-=1

class EC:   # Inato + Esp. em Combate
    nome="Combatente"
    def __init__(s): s.pv=42; s.pe=16; s.df=15; s.init=10; s.rr=True; s.refl=9; s.fort=7; s.jam=False; s.desprev=0
    def defesa(s): return s.df-(3 if s.desprev>0 else 0)
    def turno(s,o):
        if s.jam: s.jam=False; return      # acao comum pra desemperrar, sem ataque
        for i in range(2):
            bonus=9; adv=False
            if i==0 and s.pe>=2: s.pe-=2; bonus+=2; adv=True   # Precisao Definitiva + Golpe Especial Preciso
            r,h=atk(bonus,o.defesa(),adv)
            if r<=3: s.jam=True             # Pistoleiro Iniciado: emperra de 1 a 3
            if h:
                crit=(r==20)
                x=d(1,12)+d(1,6)+d(1,12)+7+((d(1,12)+d(1,6)+d(1,12)) if crit else 0)
                o.dano(x)
            if s.jam: break
    def dano(s,x):
        if s.pe>=2 and x>=10: s.pe-=2; x=max(0,x-(d(1,6)+3))  # Reforco Reativo
        s.pv-=x
    def fim(s):
        if s.desprev>0: s.desprev-=1

class RS:   # Restringido
    nome="Restringido"
    def __init__(s): s.pv=45; s.est=16; s.df=17; s.init=5; s.rr=False; s.refl=11; s.fort=6; s.foco=False; s.desprev=0; s.resil=2
    def defesa(s): return s.df-(3 if s.desprev>0 else 0)
    def turno(s,o):
        if not s.foco and s.est>=2: s.est-=2; s.foco=True
        f=2 if s.foco else 0
        # pistola principal (3o grau, Precisa) com Ataque Inconsequente
        r,h=atk(11+f,o.defesa(),adv=True); s.desprev=1
        if h:
            x=d(1,10)+5+2+2+5+(d(1,6) if s.foco else 0)
            if r==20: x+=d(1,10)+(d(1,6) if s.foco else 0)
            if o.desprev>0: x+=d(2,8)          # Ataque Furtivo
            o.dano(x)
        r,h=atk(9+f,o.defesa())                 # segunda pistola (acao bonus, sem atributo)
        if h: o.dano(d(1,10)+1+2+(d(1,6) if s.foco else 0))
    def dano(s,x):
        if s.resil>0 and x>=10: s.resil-=1; x=max(0,x-4)   # Resiliencia Imediata
        s.pv-=x
    def fim(s):
        if s.desprev>0: s.desprev-=1

def duelo(A,B):
    a,b=A(),B()
    ia=d20()+a.init; ib=d20()+b.init
    if a.rr and ia<ib: ia=max(ia,d20()+a.init)
    if b.rr and ib<ia: ib=max(ib,d20()+b.init)
    ordem=[a,b] if ia>=ib else [b,a]
    for rd in range(30):
        for x in ordem:
            o=b if x is a else a
            x.turno(o)
            if o.pv<=0: return x.nome, max(0,x.pv)/ {"Tecnico":33,"Combatente":42,"Restringido":45}[x.nome], rd+1
            x.fim()
    return "empate",0,30

random.seed(42); N=20000
placar={"Tecnico":0,"Combatente":0,"Restringido":0}
for A,B in itertools.combinations([ET,EC,RS],2):
    res=[duelo(A,B) for _ in range(N)]
    wa=sum(1 for w,_,_ in res if w==A.nome); wb=sum(1 for w,_,_ in res if w==B.nome)
    va=statistics.mean(p for w,p,_ in res if w==A.nome) if wa else 0
    vb=statistics.mean(p for w,p,_ in res if w==B.nome) if wb else 0
    placar[A.nome]+=wa; placar[B.nome]+=wb
    print(f"{A.nome:11s} x {B.nome:11s}: {100*wa/N:5.1f}% (sobra {100*va:3.0f}% PV) | {100*wb/N:5.1f}% (sobra {100*vb:3.0f}% PV) | rodadas {statistics.mean(r for _,_,r in res):.1f}")
print("Vitorias totais (de 40.000 lutas cada):", {k:f"{100*v/(2*N):.1f}%" for k,v in placar.items()})
