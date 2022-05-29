import pygame,sys,random
import msvcrt as m

############### KLASA POKEMONA OGOLEM#################################################################
class Pokemon():
    def __init__(self,is_alive,name,typ,health,speed):
        self.is_alive=True
        self.name=name
        self.typ=typ
        self.health=int(health)
        self.speed=speed
        self.current_hp=self.health
    def kill(self):
        if self.current_hp<=0:
            self.is_alive=False
            self.current_hp=0
        else:
            pass

########### Bulbasaur #################################################################
class Bulba(Pokemon):
    def __init__(self,is_alive,name='Bulbasaur',typ='Grass',health=45,speed=45):
        super().__init__(is_alive,name,typ,health,speed)
        self.health=health
        self.current_hp=health
        self.max_hp=health
        self.health_bar_lenght=200
        self.health_ratio=self.max_hp/self.health_bar_lenght
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0), (10,10,self.current_hp/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_lenght,25),4)
    def tackle(self,posx,posy):
        atak=random.randint(15,25)
        sprites=[]
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle6.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle7.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle8.png').convert_alpha()))
        current_sprite = 0
        image=sprites[int(current_sprite)]
        rect=image.get_rect(center=(posx,posy))
        #screen.blit(image,rect)
        while current_sprite<len(sprites):
            napis = game_font3.render(f'{self.name} uzyl TACKLE', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image=sprites[int(current_sprite)]
            rect=image.get_rect(center=(posx,posy))
            pygame.display.flip()
            current_sprite+=0.3
            display_walka(player,przeciwnik)
        return atak
    def vine(self,typ_przeciwnika,posx,posy):
        if typ_przeciwnika=='Water':
            atak=random.randint(25,45)
        elif typ_przeciwnika=='Fire':
            atak=random.randint(5,15)
        else:
            atak=random.randint(10,20)
        sprites = []
        sprites.append(pygame.image.load('sprites/Vine Whip/vine1.png'))
        sprites.append(pygame.image.load('sprites/Vine Whip/vine2.png'))
        sprites.append(pygame.image.load('sprites/Vine Whip/vine3.png'))
        sprites.append(pygame.image.load('sprites/Vine Whip/vine4.png'))
        sprites.append(pygame.image.load('sprites/Vine Whip/vine5.png'))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            if typ_przeciwnika=='Water':
                napis = game_font4.render(f'{self.name} uzyl VINE WHIP. To jest SUPEREFEKTYWNE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            elif typ_przeciwnika=='Fire':
                napis = game_font4.render(f'{self.name} uzyl VINE WHIP. To jest NIEEFEKTYWNE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            else:
                napis = game_font3.render(f'{self.name} uzyl VINE WHIP', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def synthesis(self,posx,posy):
        self.current_hp+=20
        if self.current_hp>45:
            self.current_hp=45
        atak=0
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn6.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/synthesis/syn7.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl SYNTHESIS', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def double(self,posx,posy):
        atak=random.randint(25,35)
        self.current_hp-=round(atak/3)
        if self.current_hp<=round(atak/3):
            self.current_hp=0
            self.is_alive=False
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/double/double1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/double/double2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/double/double3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/double/double4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/double/double5.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl DOUBLE-EDGE', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def info(self):
        print(f'\nNazwa: {self.name}')
        print(f'Typ: {self.typ}')
        print(f'HP: {self.current_hp} / 45')
        print(f'Speed: {self.speed}')

############ Charmander ####################################################
class Char(Pokemon):
    def __init__(self,is_alive,name='Charmander',typ='Fire',health=39,speed=65):
        super().__init__(is_alive,name,typ,health,speed)
        self.health=health
        self.max_hp = health
        self.current_hp = health
        self.health_bar_lenght = 200
        self.health_ratio = self.max_hp / self.health_bar_lenght
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0), (10,10,self.current_hp/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_lenght,25),4)
    def scratch(self,posx,posy):
        print(f'\n{self.name} użył Scratch')
        atak=random.randint(15,25)
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/scratch/scra1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/scratch/scra2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/scratch/scra3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/scratch/scra4.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl SCRATCH', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def ember(self,typ_przeciwnika,posx,posy,obrot):
        if typ_przeciwnika=='Water'or typ_przeciwnika=='Fire':
            atak=random.randint(5,15)
        elif typ_przeciwnika=='Grass':
            atak=random.randint(25,45)
        else:
            atak=random.randint(10,20)
        sprites = []
        sprites.append(pygame.transform.flip(pygame.image.load('sprites/Ember/ember1.png').convert_alpha(),obrot,obrot))
        sprites.append(pygame.transform.flip(pygame.image.load('sprites/Ember/ember2.png').convert_alpha(), obrot, obrot))
        sprites.append(pygame.transform.flip(pygame.image.load('sprites/Ember/ember3.png').convert_alpha(), obrot, obrot))
        sprites.append(pygame.transform.flip(pygame.image.load('sprites/Ember/ember4.png').convert_alpha(), obrot, obrot))
        sprites.append(pygame.transform.flip(pygame.image.load('sprites/Ember/ember5.png').convert_alpha(), obrot, obrot))
        sprites.append(pygame.transform.flip(pygame.image.load('sprites/Ember/ember6.png').convert_alpha(), obrot, obrot))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            if typ_przeciwnika == 'Water' or typ_przeciwnika=='Fire' :
                napis = game_font4.render(f'{self.name} uzyl EMBER. To jest NIEEFEKTYWNE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            elif typ_przeciwnika == 'Grass':
                napis = game_font4.render(f'{self.name} uzyl EMBER. To jest SUPEREFEKTYWNE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            else:
                napis = game_font3.render(f'{self.name} uzyl EMBER', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def inferno(self,posx,posy):
        szansa=random.randint(0,1)
        if szansa==0:
            atak=0
            sprites = []
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno1.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno2.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno3.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno4.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno5.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno6.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno7.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno8.png').convert_alpha()))
            current_sprite = 0
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            while current_sprite < len(sprites):
                napis = game_font4.render(f'{self.name} uzyl INFERNO.{self.name} nie trafil...', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
                #screen.blit(image, rect)
                image = sprites[int(current_sprite)]
                rect = image.get_rect(center=(posx, posy))
                pygame.display.flip()
                current_sprite += 0.3
                display_walka(player, przeciwnik)
        else:
            atak=random.randint(30,50)
            sprites = []
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno1.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno2.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno3.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno4.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno5.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno6.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno7.png').convert_alpha()))
            sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Inferno/inferno8.png').convert_alpha()))
            current_sprite = 0
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            # screen.blit(image,rect)
            while current_sprite < len(sprites):
                napis = game_font3.render(f'{self.name} uzyl INFERNO', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
                screen.blit(image, rect)
                image = sprites[int(current_sprite)]
                rect = image.get_rect(center=(posx, posy))
                pygame.display.flip()
                current_sprite += 0.3
                display_walka(player, przeciwnik)
        return atak
    def roost(self,posx,posy):
        print(f'\n{self.name} użył Roost')
        if self.current_hp<=10:
            self.current_hp=39
        else:
            self.current_hp+=10
            if self.current_hp>39:
                self.current_hp=39
        atak=0
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost6.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost7.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/roost/roost8.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl ROOST', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def info(self):
        print(f'\nNazwa: {self.name}')
        print(f'Typ: {self.typ}')
        print(f'HP: {self.current_hp} / 39')
        print(f'Speed: {self.speed}')

############ SQUIRTLE ##################################
class Squirtle(Pokemon):
    def __init__(self,is_alive,name='Squirtle',typ='Water',health=44,speed=43):
        super().__init__(is_alive,name,typ,health,speed)
        self.health=health
        self.max_hp = health
        self.current_hp = health
        self.health_bar_lenght = 200
        self.health_ratio = self.max_hp / self.health_bar_lenght
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0), (10,10,self.current_hp/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_lenght,25),4)
    def tackle(self,posx,posy):
        print(f'\n{self.name} użył Tackle')
        atak=random.randint(15,25)
        sprites=[]
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle6.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle7.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle8.png').convert_alpha()))
        current_sprite = 0
        image=sprites[int(current_sprite)]
        rect=image.get_rect(center=(posx,posy))
        #screen.blit(image,rect)
        while current_sprite<len(sprites):
            napis = game_font3.render(f'{self.name} uzyl TACKLE', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image=sprites[int(current_sprite)]
            rect=image.get_rect(center=(posx,posy))
            pygame.display.flip()
            current_sprite+=0.3
            display_walka(player,przeciwnik)
        return atak
    def water(self,typ_przeciwnika,posx,posy):
        print(f'\n{self.name} użył Water Pulse')
        if typ_przeciwnika=='Fire':
            atak=random.randint(25,45)
        elif typ_przeciwnika=='Grass' or typ_przeciwnika=='Water':
            atak=random.randint(5,15)
        else:
            atak=random.randint(10,20)
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Water Pulse/water1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Water Pulse/water2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Water Pulse/water3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Water Pulse/water4.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            if typ_przeciwnika == 'Fire':
                napis = game_font4.render(f'{self.name} uzyl WATER PULSE. To jest SUPEREFEKTYWNE', True,
                                          (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            elif typ_przeciwnika == 'Grass' or typ_przeciwnika == 'Water':
                napis = game_font4.render(f'{self.name} uzyl WATER PULSE. To jest NIEEFEKTYWNE', True,
                                          (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            else:
                napis = game_font3.render(f'{self.name} uzyl WATER PULSE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def drain(self,posx,posy):
        print(f'\n{self.name} użył Drain Punch')
        atak=random.randint(10,30)
        self.current_hp+=round(atak/2,0)
        if self.current_hp>44:
            self.current_hp=44
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Drain Punch/drain1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Drain Punch/drain2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Drain Punch/drain3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Drain Punch/drain4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Drain Punch/drain5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Drain Punch/drain6.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl DRAIN PUNCH', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def revenge(self,posx,posy):
        print(f'\n{self.name} użył Revenge')
        atak=random.randint(5,40)
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Revenge/reve1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Revenge/reve2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Revenge/reve3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Revenge/reve4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Revenge/reve5.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl REVENGE', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def info(self):
        print(f'\nNazwa: {self.name}')
        print(f'Typ: {self.typ}')
        print(f'HP: {self.current_hp} / 44')
        print(f'Speed: {self.speed}')

####### Caterpie ##################################################
class Caterpie(Pokemon):
    def __init__(self,is_alive,name='Caterpie',typ='Grass',health=20,speed=40):
        super().__init__(is_alive,name,typ,health,speed)
        self.health=health
        self.max_hp = health
        self.current_hp = health
        self.health_bar_lenght = 200
        self.health_ratio = self.max_hp / self.health_bar_lenght
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0), (10,10,self.current_hp/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_lenght,25),4)
    def string(self):
        print(f'\n{self.name} użył String-Shot')
        atak=0
        sprites = []
        sprites.append(pygame.image.load('sprites/String Shot/string1.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/String Shot/string2.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/String Shot/string3.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/String Shot/string4.png').convert_alpha())
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(550, 500))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl STRING-SHOT', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(550, 500))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def tackle(self,posx,posy):
        print(f'\n{self.name} użył Tackle')
        atak=random.randint(10,20)
        sprites=[]
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle6.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle7.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle8.png').convert_alpha()))
        current_sprite = 0
        image=sprites[int(current_sprite)]
        rect=image.get_rect(center=(posx,posy))
        #screen.blit(image,rect)
        while current_sprite<len(sprites):
            napis = game_font3.render(f'{self.name} uzyl TACKLE', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image=sprites[int(current_sprite)]
            rect=image.get_rect(center=(posx,posy))
            pygame.display.flip()
            current_sprite+=0.3
            display_walka(player,przeciwnik)
        return atak
    def bug(self,typ_przeciwnika):
        print(f'\n{self.name} użył Bug Bite')
        if typ_przeciwnika=='Grass':
            atak=random.randint(15,25)
        elif typ_przeciwnika=='Fire':
            atak=random.randint(5,10)
        else:
            atak=random.randint(10,20)
        sprites = []
        sprites.append(pygame.image.load('sprites/Bug Bite/bug1.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Bug Bite/bug2.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Bug Bite/bug3.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Bug Bite/bug4.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Bug Bite/bug5.png').convert_alpha())
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(550, 500))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            if typ_przeciwnika == 'Grass':
                napis = game_font4.render(f'{self.name} uzyl BUG BITE. To jest SUPEREFEKTYWNE', True,
                                          (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            elif typ_przeciwnika == 'Fire':
                napis = game_font4.render(f'{self.name} uzyl BUG BITE. To jest NIEEFEKTYWNE', True,
                                          (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            else:
                napis = game_font3.render(f'{self.name} uzyl BUG BITE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(550, 500))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def info(self):
        print(f'\nNazwa: {self.name}')
        print(f'Typ: {self.typ}')
        print(f'HP: {self.current_hp} / 20')
        print(f'Speed: {self.speed}')
    ###### Torkoal ####################################################

###### Torkoal ##################################################
class Torkoal(Pokemon):
    def __init__(self,is_alive,name='Torkoal',typ='Fire',health=50,speed=20):
        super().__init__(is_alive,name,typ,health,speed)
        self.health=health
        self.max_hp = health
        self.current_hp = health
        self.health_bar_lenght = 200
        self.health_ratio = self.max_hp / self.health_bar_lenght
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0), (10,10,self.current_hp/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_lenght,25),4)
    def ember(self,typ_przeciwnika,posx,posy,obrot):
        print(f'\n{self.name} użył Ember')
        if typ_przeciwnika=='Water'or typ_przeciwnika=='Fire':
            atak=random.randint(5,10)
        elif typ_przeciwnika=='Grass':
            atak=random.randint(15,25)
        else:
            atak=random.randint(10,20)
        sprites = []
        sprites.append(
            pygame.transform.flip(pygame.image.load('sprites/Ember/ember1.png').convert_alpha(), obrot, obrot))
        sprites.append(
            pygame.transform.flip(pygame.image.load('sprites/Ember/ember2.png').convert_alpha(), obrot, obrot))
        sprites.append(
            pygame.transform.flip(pygame.image.load('sprites/Ember/ember3.png').convert_alpha(), obrot, obrot))
        sprites.append(
            pygame.transform.flip(pygame.image.load('sprites/Ember/ember4.png').convert_alpha(), obrot, obrot))
        sprites.append(
            pygame.transform.flip(pygame.image.load('sprites/Ember/ember5.png').convert_alpha(), obrot, obrot))
        sprites.append(
            pygame.transform.flip(pygame.image.load('sprites/Ember/ember6.png').convert_alpha(), obrot, obrot))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(posx, posy))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            if typ_przeciwnika == 'Water' or typ_przeciwnika=='Fire' :
                napis = game_font4.render(f'{self.name} uzyl EMBER. To jest NIEEFEKTYWNE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            elif typ_przeciwnika == 'Grass':
                napis = game_font4.render(f'{self.name} uzyl EMBER. To jest SUPEREFEKTYWNE', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            else:
                napis = game_font3.render(f'{self.name} uzyl EMBER', True, (255, 255, 255))
                napis_rect = napis.get_rect(topleft=(50, 650))
                screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(posx, posy))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def destruct(self):
        print(f'\n{self.name} użył Self-Destruct')
        self.current_hp=0
        self.is_alive=False
        atak=30
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Self Destruct/self1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Self Destruct/self2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Self Destruct/self3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Self Destruct/self4.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(900, 275))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl SELF-DESTRUCT', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(900, 275))
            pygame.display.flip()
            current_sprite += 0.2
            display_walka(player, przeciwnik)
        return atak
    def gyro(self,typ_przeciwnika):
        print(f'\n{self.name} użył Gyro Ball')
        if typ_przeciwnika=='Fire':
            atak=5
        else:
            atak=15
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Gyro Ball/gyro1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Gyro Ball/gyro2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Gyro Ball/gyro3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Gyro Ball/gyro4.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(550, 500))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl GYRO BALL', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(550, 500))
            pygame.display.flip()
            current_sprite += 0.2
            display_walka(player, przeciwnik)
        return atak
    def heat(self):
        print(f'\n{self.name} użył Heath Heal')
        self.current_hp+=self.max_hp/3
        if self.current_hp>50:
            self.current_hp=50
        atak=0
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Heat Heal/heat1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Heat Heal/heat2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Heat Heal/heat3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Heat Heal/heat4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Heat Heal/heat5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Heat Heal/heat6.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(900, 275))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl HEAT HEAL', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(900, 275))
            pygame.display.flip()
            current_sprite += 0.2
            display_walka(player, przeciwnik)
        return atak
    def info(self):
        print(f'\nNazwa: {self.name}')
        print(f'Typ: {self.typ}')
        print(f'HP: {self.current_hp} / 50')
        print(f'Speed: {self.speed}')

################################### Magikarp ############
class Magikarp(Pokemon):
    def __init__(self,is_alive,name='Magikarp',typ='Water',health=20,speed=80):
        super().__init__(is_alive,name,typ,health,speed)
        self.health=health
        self.max_hp = health
        self.current_hp = health
        self.health_bar_lenght = 200
        self.health_ratio = self.max_hp / self.health_bar_lenght
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0), (10,10,self.current_hp/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_lenght,25),4)
    def splash(self):
        atak=0
        sprites = []
        sprites.append(pygame.image.load('sprites/Splash/splash1.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash2.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash3.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash4.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash5.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash6.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash7.png').convert_alpha())
        sprites.append(pygame.image.load('sprites/Splash/splash8.png').convert_alpha())
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(900, 275))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl SPLASH', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(900, 275))
            pygame.display.flip()
            current_sprite += 0.15
            display_walka(player, przeciwnik)
        return atak
    def flai(self):
        atak=self.current_hp
        sprites = []
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Flai/flai1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Flai/flai2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Flai/flai3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Flai/flai4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/Flai/flai5.png').convert_alpha()))
        current_sprite = 0
        image = sprites[int(current_sprite)]
        rect = image.get_rect(center=(550, 500))
        # screen.blit(image,rect)
        while current_sprite < len(sprites):
            napis = game_font3.render(f'{self.name} uzyl FLAI', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image = sprites[int(current_sprite)]
            rect = image.get_rect(center=(550, 500))
            pygame.display.flip()
            current_sprite += 0.3
            display_walka(player, przeciwnik)
        return atak
    def tackle(self,posx,posy):
        print(f'\n{self.name} użył Tackle')
        atak=random.randint(10,20)
        sprites=[]
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle1.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle2.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle3.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle4.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle5.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle6.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle7.png').convert_alpha()))
        sprites.append(pygame.transform.scale2x(pygame.image.load('sprites/tackle/tackle8.png').convert_alpha()))
        current_sprite = 0
        image=sprites[int(current_sprite)]
        rect=image.get_rect(center=(posx,posy))
        #screen.blit(image,rect)
        while current_sprite<len(sprites):
            napis = game_font3.render(f'{self.name} uzyl TACKLE', True, (255, 255, 255))
            napis_rect = napis.get_rect(topleft=(50, 650))
            screen.blit(napis, napis_rect)
            screen.blit(image, rect)
            image=sprites[int(current_sprite)]
            rect=image.get_rect(center=(posx,posy))
            pygame.display.flip()
            current_sprite+=0.3
            display_walka(player,przeciwnik)
        return atak
    def info(self):
        print(f'\nNazwa: {self.name}')
        print(f'Typ: {self.typ}')
        print(f'HP: {self.current_hp} / 20')
        print(f'Speed: {self.speed}')
################## PRZYCISKI ############################
class Button():
    def __init__(self,image,position):
        self.image=image
        self.rect=image.get_rect(topleft= position)
        self.clicked=False
    def draw(self):
        screen.blit(self.image,self.rect)
        action=False
        #get position
        pos=pygame.mouse.get_pos()
        # mouseover and warunki
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        return action
########### FUNKCJE GRY ###################################
def wait():
    m.getch()
def wybor_pokemona_display():
    screen.blit(scena, (370, 200))
    screen.blit(pokeball1, p1)
    screen.blit(pokeball2, p2)
    screen.blit(pokeball3, p3)
    ##### Napis
    wybor_surface1 = game_font1.render(f'Witam w grze PythonPokemon!', True, (255, 255, 255))
    wybor_rect1 = wybor_surface1.get_rect(center=(640, 100))
    wybor_surface2 = game_font1.render(f'W pokeballach pod Toba sa pokemony, kliknij na swojego faworyta', True,
                                       (255, 255, 255))
    wybor_rect2 = wybor_surface2.get_rect(center=(640, 150))
    screen.blit(wybor_surface1, wybor_rect1)
    screen.blit(wybor_surface2, wybor_rect2)
    #### pokemony
    # bulbasaur
    bulba = Bulba(True)
    bnazwa = game_font1.render(f'Nazwa: {bulba.name}', True, (255, 255, 255))
    bnazwa_rect = bnazwa.get_rect(center=(425, 550))
    btyp = game_font1.render(f'Typ: {bulba.typ}', True, (255, 255, 255))
    btyp_rect = btyp.get_rect(center=(425, 585))
    bhp = game_font1.render(f'HP: {bulba.health}', True, (255, 255, 255))
    bhp_rect = bhp.get_rect(center=(425, 620))
    bspeed = game_font1.render(f'Speed: {bulba.speed}', True, (255, 255, 255))
    bspeed_rect = bspeed.get_rect(center=(425, 655))
    screen.blit(bnazwa, bnazwa_rect)
    screen.blit(btyp, btyp_rect)
    screen.blit(bhp, bhp_rect)
    screen.blit(bspeed, bspeed_rect)
    # charmander
    char = Char(True)
    cnazwa = game_font1.render(f'Nazwa: {char.name}', True, (255, 255, 255))
    cnazwa_rect = bnazwa.get_rect(center=(625, 550))
    ctyp = game_font1.render(f'Typ: {char.typ}', True, (255, 255, 255))
    ctyp_rect = btyp.get_rect(center=(625, 585))
    chp = game_font1.render(f'HP: {char.health}', True, (255, 255, 255))
    chp_rect = bhp.get_rect(center=(625, 620))
    cspeed = game_font1.render(f'Speed: {char.speed}', True, (255, 255, 255))
    cspeed_rect = bspeed.get_rect(center=(625, 655))
    screen.blit(cnazwa, cnazwa_rect)
    screen.blit(ctyp, ctyp_rect)
    screen.blit(chp, chp_rect)
    screen.blit(cspeed, cspeed_rect)
    # squrtle
    squir = Squirtle(True)
    snazwa = game_font1.render(f'Nazwa: {squir.name}', True, (255, 255, 255))
    snazwa_rect = bnazwa.get_rect(center=(850, 550))
    styp = game_font1.render(f'Typ: {squir.typ}', True, (255, 255, 255))
    styp_rect = btyp.get_rect(center=(850, 585))
    shp = game_font1.render(f'HP: {squir.health}', True, (255, 255, 255))
    shp_rect = bhp.get_rect(center=(850, 620))
    sspeed = game_font1.render(f'Speed: {squir.speed}', True, (255, 255, 255))
    sspeed_rect = bspeed.get_rect(center=(850, 655))
    screen.blit(snazwa, snazwa_rect)
    screen.blit(styp, styp_rect)
    screen.blit(shp, shp_rect)
    screen.blit(sspeed, sspeed_rect)
def wybor_pokemona():
    if pok1.draw():
        ##############
        screen.blit(bg_surface, (0, 0))
        pok=Bulba(True)
        return Bulba(True)
    elif  pok2.draw():
        screen.blit(bg_surface, (0, 0))
        return Char(True)
    elif pok3.draw():
        screen.blit(bg_surface, (0, 0))
        return Squirtle(True)
def gratulowanie_wyboru(player):
    screen.blit(sycamore, (0, 0))
    wybor_surface1 = game_font1.render(f'Gratuluje wyboru pokemona!', True, (255, 255, 255))
    wybor_rect1 = wybor_surface1.get_rect(center=(780, 100))
    wybor_surface2 = game_font1.render(f'Mam nadzieje, ze Ty i {player.name} przyzyjecie wiele cudownych przygód!', True,
                                       (255, 255, 255))
    wybor_rect2 = wybor_surface2.get_rect(center=(840, 150))
    screen.blit(wybor_surface1, wybor_rect1)
    screen.blit(wybor_surface2, wybor_rect2)
    wybor_surface3 = game_font1.render(f'Za chwile zaczniesz swoja przygode! Nacisnij SPACJE zeby kontynuowac', True, (255, 255, 255))
    if player.name=='Bulbasaur':
        wybor_surface11 = game_font1.render(f'---Ataki {player.name}a:---', True, (255, 255, 255))
        wybor_rect11 = wybor_surface1.get_rect(center=(800, 250))
        screen.blit(wybor_surface11, wybor_rect11)
        wybor_surface12 = game_font1.render(f'---TACKLE- Zwykly atak zadajacy pomiedzy 15 a 25 obrazen---', True, (255, 255, 255))
        wybor_rect12 = wybor_surface1.get_rect(center=(640, 350))
        screen.blit(wybor_surface12, wybor_rect12)
        wybor_surface13 = game_font1.render(f'---VINE WHIP- Efektywny przeciwko pokemonom WODNYM, nieefektywny przeciwko OGNISTYM---', True,(255, 255, 255))
        wybor_rect13 = wybor_surface1.get_rect(center=(440, 400))
        screen.blit(wybor_surface13, wybor_rect13)
        wybor_surface14 = game_font1.render(f'---SYNTHESIS- Leczy 20 punktow zycia---', True, (255, 255, 255))
        wybor_rect14 = wybor_surface1.get_rect(center=(740, 450))
        screen.blit(wybor_surface14, wybor_rect14)
        wybor_surface13 = game_font1.render(f'--DOUBLE-EDGE- Silny atak zadajacy pomiedzy 25-30, ale rani {player.name}a za 1/3 zadanych obrazen---', True,(255, 255, 255))
        wybor_rect13 = wybor_surface1.get_rect(center=(400, 500))
        screen.blit(wybor_surface13, wybor_rect13)
    elif player.name=='Charmander':
        wybor_surface11 = game_font1.render(f'---Ataki {player.name}a:---', True, (255, 255, 255))
        wybor_rect11 = wybor_surface1.get_rect(center=(800, 250))
        screen.blit(wybor_surface11, wybor_rect11)
        wybor_surface12 = game_font1.render(f'---SCRATCH- Zwykly atak zadajacy pomiedzy 15 a 25 obrazen---', True,
                                            (255, 255, 255))
        wybor_rect12 = wybor_surface1.get_rect(center=(640, 350))
        screen.blit(wybor_surface12, wybor_rect12)
        wybor_surface13 = game_font1.render(
            f'---EMBER- Efektywny przeciwko pokemonom ROSLINNYM, nieefektywny przeciwko WODNYM---', True,
            (255, 255, 255))
        wybor_rect13 = wybor_surface1.get_rect(center=(440, 400))
        screen.blit(wybor_surface13, wybor_rect13)
        wybor_surface14 = game_font1.render(f'---INFERNO- Leczy 20 potezny atak zadajacy 30-50 obrazen, ale jego celnosc to 50 procent--', True, (255, 255, 255))
        wybor_rect14 = wybor_surface1.get_rect(center=(440, 450))
        screen.blit(wybor_surface14, wybor_rect14)
        wybor_surface13 = game_font1.render(
            f'---ROOST- Jesli {player.name} ma <10HP leczy cale zycie, w innym przypadku leczy 10HP--',
            True, (255, 255, 255))
        wybor_rect13 = wybor_surface1.get_rect(center=(500, 500))
        screen.blit(wybor_surface13, wybor_rect13)
    elif player.name=='Squirtle':
        wybor_surface11 = game_font1.render(f'---Ataki {player.name}a:---', True, (255, 255, 255))
        wybor_rect11 = wybor_surface1.get_rect(center=(800, 250))
        screen.blit(wybor_surface11, wybor_rect11)
        wybor_surface12 = game_font1.render(f'---TACKLE- Zwykly atak zadajacy pomiedzy 15 a 25 obrazen---', True, (255, 255, 255))
        wybor_rect12 = wybor_surface1.get_rect(center=(640, 350))
        screen.blit(wybor_surface12, wybor_rect12)
        wybor_surface13 = game_font1.render(
            f'---WATER PULSE- Efektywny przeciwko OGNISTYM, nieefektywny przeciwko ROSLINNYM---', True,
            (255, 255, 255))
        wybor_rect13 = wybor_surface1.get_rect(center=(440, 400))
        screen.blit(wybor_surface13, wybor_rect13)
        wybor_surface14 = game_font1.render(f'---DRAIN PUNCH- Atak zadajacy od 10 do 30 obrazen, leczy on za polowe zadanych obrazen--', True, (255, 255, 255))
        wybor_rect14 = wybor_surface1.get_rect(center=(440, 450))
        screen.blit(wybor_surface14, wybor_rect14)
        wybor_surface13 = game_font1.render(
            f'---REVENGE- Potezny atak z duzym rozstrzalem obrazen, zadaje pomiedzy 5 a 40 obrazen--',
            True, (255, 255, 255))
        wybor_rect13 = wybor_surface1.get_rect(center=(440, 500))
        screen.blit(wybor_surface13, wybor_rect13)
    wybor_rect3 = wybor_surface3.get_rect(center=(840, 700))
    screen.blit(wybor_surface3, wybor_rect3)
def przypisanie_przeciwnika():
    i=random.randint(1,12)
    if i == 1 or i == 2 or i == 3:
        przeciwnik = Caterpie(True)
    elif i == 4:
        przeciwnik = Bulba(True)
    elif i == 5 or i == 6 or i == 7:
        przeciwnik = Torkoal(True)
    elif i == 8:
        przeciwnik = Char(True)
    elif i == 9 or i == 10 or i == 11:
        przeciwnik = Magikarp(True)
    elif i==12:
        przeciwnik=Squirtle(True)
    else:
        pass
    return przeciwnik
def ekran_przed_walka(runda,przeciwnik):
    wybor_surface1 = game_font2.render(f'Runda: {runda} !', True, (255, 255, 255))
    wybor_rect1 = wybor_surface1.get_rect(center=(640, 300))
    screen.blit(wybor_surface1,wybor_rect1)
    wybor_surface2 = game_font2.render(f'Zaatakowal Cie dziki {przeciwnik.name}', True, (255, 255, 255))
    wybor_rect2 = wybor_surface2.get_rect(center=(640, 400))
    screen.blit(wybor_surface2,wybor_rect2)
    wybor_surface3 = game_font1.render(f'Nacisnij SPACJE zeby kontynuowac', True, (255, 255, 255))
    wybor_rect3 = wybor_surface2.get_rect(center=(840, 500))
    screen.blit(wybor_surface3, wybor_rect3)
def display_walka(player,przeciwnik):
    screen.blit(battle_surface,(0,0))
    if player.name=='Bulbasaur':
        screen.blit(bulba_tyl,(200,150))
        pygame.draw.rect(screen,(255,0,0), (500,375,player.current_hp/player.health_ratio,20))
        pygame.draw.rect(screen,(0,0,0),(500,375,player.health_bar_lenght,20),4)
        screen.blit(bulba_ataki, (1000,460) )
    elif player.name=='Squirtle':
        screen.blit(squirt_tyl,(200,150))
        pygame.draw.rect(screen,(255,0,0), (500,340,player.current_hp/player.health_ratio,20))
        pygame.draw.rect(screen,(0,0,0),(500,340,player.health_bar_lenght,20),4)
        screen.blit(bulba_ataki, (1000,460))
    elif player.name=='Charmander':
        screen.blit(char_tyl,(200,150))
        pygame.draw.rect(screen,(255,0,0), (550,360,player.current_hp/player.health_ratio,20))
        pygame.draw.rect(screen,(0,0,0),(550,360,player.health_bar_lenght,20),4)
        screen.blit(char_ataki,(1000,460))
    if przeciwnik.name=='Bulbasaur':
        screen.blit(bulba_przod, (750, 75))
        pygame.draw.rect(screen,(255,0,0), (850,170,przeciwnik.current_hp/przeciwnik.health_ratio,17))
        pygame.draw.rect(screen,(0,0,0),(850,170,przeciwnik.health_bar_lenght,17),4)
    elif przeciwnik.name=='Squirtle':
        screen.blit(squirt_przod,(750, 75))
        pygame.draw.rect(screen,(255,0,0), (820,160,przeciwnik.current_hp/przeciwnik.health_ratio,17))
        pygame.draw.rect(screen,(0,0,0),(820,160,przeciwnik.health_bar_lenght,17),4)
    elif przeciwnik.name=='Charmander':
        screen.blit(char_przod,(750, 75))
        pygame.draw.rect(screen,(255,0,0), (790,120,przeciwnik.current_hp/przeciwnik.health_ratio,17))
        pygame.draw.rect(screen,(0,0,0),(790,120,przeciwnik.health_bar_lenght,17),4)
    elif przeciwnik.name=='Caterpie':
        screen.blit(cater,(750, 75))
        pygame.draw.rect(screen,(255,0,0), (825,170,przeciwnik.current_hp/przeciwnik.health_ratio,17))
        pygame.draw.rect(screen,(0,0,0),(825,170,przeciwnik.health_bar_lenght,17),4)
    elif przeciwnik.name=='Torkoal':
        screen.blit(tork,(750, 50))
        pygame.draw.rect(screen,(255,0,0), (840,150,przeciwnik.current_hp/przeciwnik.health_ratio,17))
        pygame.draw.rect(screen,(0,0,0),(840,150,przeciwnik.health_bar_lenght,17),4)
    elif przeciwnik.name=='Magikarp':
        screen.blit(magi,(750, 75))
        pygame.draw.rect(screen,(255,0,0), (840,140,przeciwnik.current_hp/przeciwnik.health_ratio,17))
        pygame.draw.rect(screen,(0,0,0),(840,140,przeciwnik.health_bar_lenght,17),4)
    screen.blit(text_window, (0, 600))
def player_ruch(player):
                if player.name == 'Bulbasaur':
                    if bulba_tackleb.draw():
                        atak = player.tackle(900,275)
                        return atak
                    elif bulba_vineb.draw():
                        atak = player.vine(typ_przeciwnika,900,275)
                        return atak
                    elif bulba_synb.draw():
                        atak = player.synthesis(550,500)
                        return atak
                    elif bulba_doubleb.draw():
                        atak = player.double(900,275)
                        return atak
                elif player.name == 'Charmander':
                    if char_scratchb.draw():
                        atak = player.scratch(900,275)
                        return atak
                    elif char_emberb.draw():
                        atak = player.ember(typ_przeciwnika,900,275,False)
                        return atak
                    elif char_infernob.draw():
                        atak = player.inferno(900,275)
                        return atak
                    elif char_roostb.draw():
                        atak = player.roost(550,500)
                        return atak
                else:
                    if squirt_tackleb.draw():
                        atak = player.tackle(900,275)
                        return atak
                    elif squirt_waterb.draw():
                        atak = player.water(typ_przeciwnika,900,275)
                        return atak
                    elif squirt_drainb.draw():
                        atak = player.drain(900,275)
                        return atak
                    elif squirt_revengeb.draw():
                        atak = player.revenge(900,275)
                        return atak
def przeciwnik_ruch(przeciwnik):
    i=random.randint(1,4)
    if przeciwnik.name=='Caterpie':
        if i==1:
            atak=przeciwnik.string()
        elif i==2:
            atak=przeciwnik.string()
        elif i==3:
            atak=przeciwnik.tackle(550,500)
        else:
            atak=przeciwnik.bug(typ_playera)
    elif przeciwnik.name=='Torkoal':
        if i==1:
            atak = przeciwnik.ember(typ_playera, 550, 500, True)
        elif i==2:
            atak=przeciwnik.destruct()
        elif i==3:
            atak=przeciwnik.gyro(typ_playera)
        else:
            atak=przeciwnik.heat()
    elif przeciwnik.name=='Magikarp':
        if i==1:
            atak=przeciwnik.splash()
        elif i==2:
            atak=przeciwnik.splash()
        elif i==3:
            atak=przeciwnik.tackle(550,500)
        else:
            atak=przeciwnik.flai()
    elif przeciwnik.name=='Bulbasaur':
        if i==1:
            atak=przeciwnik.tackle(550,500)
        elif i==2:
            atak=przeciwnik.vine(typ_playera,550,500)
        elif i==3:
            atak=przeciwnik.synthesis(900,275)
        else:
            atak=przeciwnik.double(550,500)
    elif przeciwnik.name=='Charmander':
        if i==1:
            atak=przeciwnik.scratch(550,500)
        elif i==2:
            atak=przeciwnik.ember(typ_playera,550,500,True)
        elif i==3:
            atak=przeciwnik.inferno(550,500)
        else:
            atak=przeciwnik.roost(900,275)
    else:
        if i==1:
            atak=przeciwnik.tackle(550,500)
        elif i==2:
            atak=przeciwnik.water(typ_playera,550,500)
        elif i==3:
            atak=przeciwnik.drain(550,500)
        else:
            atak=przeciwnik.revenge(550,500)
    return atak
def walka(player,przeciwnik,typ_playera,typ_przeciwnika):
    if przeciwnik.is_alive and player.is_alive:
        if player.name=='Bulbasaur':
                #if bulba_tackleb.draw() or bulba_vineb.draw() or bulba_doubleb.draw() or bulba_synb.draw():
                    if player.speed>przeciwnik.speed:
                            atak_playera=player_ruch(player)
                            if atak_playera!=None:
                                przeciwnik.current_hp-=atak_playera
                                player.kill()
                                przeciwnik.kill()
                                if przeciwnik.is_alive:
                                    atak_przeciwnika=przeciwnik_ruch(przeciwnik)
                                    player.current_hp-=atak_przeciwnika
                                    player.kill()
                                    przeciwnik.kill()
                            else:
                                pass
                    elif player.speed<przeciwnik.speed:
                        atak_playera=player_ruch(player)
                        if atak_playera!=None :
                            atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                            player.current_hp -= atak_przeciwnika
                            player.kill()
                            przeciwnik.kill()
                            if player.is_alive:
                                    przeciwnik.current_hp -= atak_playera
                                    player.kill()
                                    przeciwnik.kill()
                        else:
                            pass
                    else:
                        i=random.randint(0,1)
                        if i==0:
                            atak_playera = player_ruch(player)
                            if atak_playera != None:
                                przeciwnik.current_hp -= atak_playera
                                player.kill()
                                przeciwnik.kill()
                                if przeciwnik.is_alive:
                                    atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                                    player.current_hp -= atak_przeciwnika
                                    player.kill()
                                    przeciwnik.kill()
                            else:
                                pass
                        else:
                            atak_playera = player_ruch(player)
                            if atak_playera != None:
                                atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                                player.current_hp -= atak_przeciwnika
                                player.kill()
                                przeciwnik.kill()
                                if player.is_alive:
                                    przeciwnik.current_hp -= atak_playera
                                    player.kill()
                                    przeciwnik.kill()
                            else:
                                pass
                 #   pygame.event.wait()
        elif player.name=='Charmander':
            #if char_scratchb.draw() or char_emberb.draw() or char_infernob.draw() or char_roostb.draw():
            if player.speed > przeciwnik.speed:
                atak_playera = player_ruch(player)
                if atak_playera != None:
                    przeciwnik.current_hp -= atak_playera
                    player.kill()
                    przeciwnik.kill()
                    if przeciwnik.is_alive:
                        atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                        player.current_hp -= atak_przeciwnika
                        player.kill()
                        przeciwnik.kill()
                else:
                    pass
            elif player.speed < przeciwnik.speed:
                atak_playera = player_ruch(player)
                if atak_playera != None:
                    atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                    player.current_hp -= atak_przeciwnika
                    player.kill()
                    przeciwnik.kill()
                    if player.is_alive:
                        przeciwnik.current_hp -= atak_playera
                        player.kill()
                        przeciwnik.kill()
                else:
                    pass
            else:
                i = random.randint(0, 1)
                if i == 0:
                    atak_playera = player_ruch(player)
                    if atak_playera != None:
                        przeciwnik.current_hp -= atak_playera
                        player.kill()
                        przeciwnik.kill()
                        if przeciwnik.is_alive:
                            atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                            player.current_hp -= atak_przeciwnika
                            player.kill()
                            przeciwnik.kill()
                    else:
                        pass
                else:
                    atak_playera = player_ruch(player)
                    if atak_playera != None:
                        atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                        player.current_hp -= atak_przeciwnika
                        player.kill()
                        przeciwnik.kill()
                        if player.is_alive:
                            przeciwnik.current_hp -= atak_playera
                            player.kill()
                            przeciwnik.kill()
                    else:
                        pass
        elif player.name=='Squirtle':
            #if squirt_tackleb.draw() or squirt_waterb.draw() or squirt_drainb.draw() or squirt_revengeb.draw():
            if player.speed > przeciwnik.speed:
                atak_playera = player_ruch(player)
                if atak_playera != None:
                    przeciwnik.current_hp -= atak_playera
                    player.kill()
                    przeciwnik.kill()
                    if przeciwnik.is_alive:
                        atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                        player.current_hp -= atak_przeciwnika
                        player.kill()
                        przeciwnik.kill()
                else:
                    pass
            elif player.speed < przeciwnik.speed:
                atak_playera = player_ruch(player)
                if atak_playera != None:
                    atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                    player.current_hp -= atak_przeciwnika
                    player.kill()
                    przeciwnik.kill()
                    if player.is_alive:
                        przeciwnik.current_hp -= atak_playera
                        player.kill()
                        przeciwnik.kill()
                else:
                    pass
            else:
                i = random.randint(0, 1)
                if i == 0:
                    atak_playera = player_ruch(player)
                    if atak_playera != None:
                        przeciwnik.current_hp -= atak_playera
                        player.kill()
                        przeciwnik.kill()
                        if przeciwnik.is_alive:
                            atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                            player.current_hp -= atak_przeciwnika
                            player.kill()
                            przeciwnik.kill()
                    else:
                        pass
                else:
                    atak_playera = player_ruch(player)
                    if atak_playera != None:
                        atak_przeciwnika = przeciwnik_ruch(przeciwnik)
                        player.current_hp -= atak_przeciwnika
                        player.kill()
                        przeciwnik.kill()
                        if player.is_alive:
                            przeciwnik.current_hp -= atak_playera
                            player.kill()
                            przeciwnik.kill()
                    else:
                        pass
    else:
        return False
def porazka(runda,przeciwnik,player):
    wybor_surface1 = game_font2.render(f'Po ciezkim boju...Niezliczonych ranach...', True, (255, 255, 255))
    wybor_rect1 = wybor_surface1.get_rect(center=(540, 100))
    screen.blit(wybor_surface1,wybor_rect1)
    wybor_surface4 = game_font2.render(f'I wielu wspanialych walkach...', True, (255, 255, 255))
    wybor_rect4 = wybor_surface1.get_rect(center=(540, 200))
    screen.blit(wybor_surface4,wybor_rect4)
    wybor_surface3 = game_font2.render(f'Twoj {player.name} polegl w walce z {przeciwnik.name}...', True, (255, 255, 255))
    wybor_rect3 = wybor_surface1.get_rect(center=(550, 350))
    screen.blit(wybor_surface3,wybor_rect3)
    wybor_surface2 = game_font2.render(f'Udalo Ci sie dotrwac do {runda} rundy!', True, (255, 255, 255))
    wybor_rect2 = wybor_surface2.get_rect(center=(640, 450))
    screen.blit(wybor_surface2, wybor_rect2)
    wybor_surface5 = game_font1.render(f'*Nacisnij (ENTER) aby kontynuowac*', True, (255, 255, 255))
    wybor_rect5 = wybor_surface2.get_rect(center=(500, 550))
    screen.blit(wybor_surface5, wybor_rect5)
    wybor_surface6 = game_font1.render(f'*Lub (ESC) aby przejsc do napisow koncowych*', True, (255, 255, 255))
    wybor_rect6 = wybor_surface2.get_rect(center=(500, 600))
    screen.blit(wybor_surface6, wybor_rect6)
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RETURN:
            return True
        elif event.key==pygame.K_ESCAPE:
            return False
#####################################################################
pygame.mixer.pre_init(frequency=44100,size=-16,channels=5,buffer=512)
########################################## INICJUJEMY PYGAMEA ####################################################
pygame.init()

############ Ekran #########
screen=pygame.display.set_mode((1280,720))
############ Zmienne ##################
#CZCIONKI
game_font1=pygame.font.Font('Pokemon Hollow.ttf',20)
game_font2=pygame.font.Font('Pokemon Hollow.ttf',50)
game_font3=pygame.font.Font('Pokemon_Classic.ttf',25)
game_font4=pygame.font.Font('Pokemon_Classic.ttf',20)
#ZMIENNE GRY
pos=(0,0)
#TŁO
bg_surface=pygame.image.load('sprites/black.png')
bg_surface=pygame.transform.scale2x(bg_surface)
bg_surface=pygame.transform.scale2x(bg_surface)
#TŁO WALKI
battle_surface=pygame.image.load('sprites/back.png')
#TEXT WINDOW
text_window=pygame.image.load('text.png')
text_window=pygame.transform.scale(text_window,(1000,120))

#KONIEC
end_surface=pygame.image.load('koniec.png')
#Start
start_surface=pygame.image.load('start.png')
##### POKEMONY ###############################
### BULBASAUR
#PRZOD
bulba_przod=pygame.image.load('sprites/bulbaP.png').convert()
bulba_przod=pygame.transform.scale2x(bulba_przod)
bulba_przod=pygame.transform.scale2x(bulba_przod)
#TYL
bulba_tyl=pygame.image.load('sprites/bulbaB.png').convert()
bulba_tyl=pygame.transform.scale2x(bulba_tyl)
bulba_tyl=pygame.transform.scale2x(bulba_tyl)
bulba_tyl=pygame.transform.scale2x(bulba_tyl)
#ATAKI
bulba_ataki=pygame.image.load('sprites/bulbaataki.png').convert()
bulba_ataki=pygame.transform.scale2x(bulba_ataki)
#TACKLE
bulba_tackle=pygame.image.load('sprites/bulba_tackle.png').convert()
bulba_tackle=pygame.transform.scale2x(bulba_tackle)
bulba_tackle_rect=bulba_tackle.get_rect(center=(1140,520))
bulba_tackleb=Button(bulba_tackle,(1003,494))
#VINE WHIP
bulba_vine=pygame.image.load('sprites/bulba_vine.png').convert()
bulba_vine=pygame.transform.scale2x(bulba_vine)
bulba_vine_rect=bulba_vine.get_rect(center=(1140,575))
bulba_vineb=Button(bulba_vine,(1003,549))
#DOUBLE EDGE
bulba_double=pygame.image.load('sprites/bulba_double.png').convert()
bulba_double=pygame.transform.scale2x(bulba_double)
bulba_double_rect=bulba_double.get_rect(center=(1141,630))
bulba_doubleb=Button(bulba_double,(1000,604))
#SYNTHESIS
bulba_syn=pygame.image.load('sprites/bulba_synthesis.png').convert()
bulba_syn=pygame.transform.scale2x(bulba_syn)
bulba_syn_rect=bulba_syn.get_rect(center=(1141,685))
bulba_synb=Button(bulba_syn,(1003,659))
### CHARMANDER
#PRZOD
char_przod=pygame.image.load('sprites/charmanderP.png').convert()
char_przod=pygame.transform.scale2x(char_przod)
char_przod=pygame.transform.scale2x(char_przod)
#TYL
char_tyl=pygame.image.load('sprites/charmanderB.png').convert()
char_tyl=pygame.transform.scale2x(char_tyl)
char_tyl=pygame.transform.scale2x(char_tyl)
char_tyl=pygame.transform.scale2x(char_tyl)
##ATAKI
char_ataki=pygame.image.load('sprites/charataki.png').convert()
char_ataki=pygame.transform.scale2x(char_ataki)
#SCRATCH
char_scratch=pygame.image.load('sprites/char_scratch.png').convert()
char_scratch=pygame.transform.scale2x(char_scratch)
char_scratch_rect=char_scratch.get_rect(center=(1140,520))
char_scratchb=Button(char_scratch,(1003,494))
#EMBER
char_ember=pygame.image.load('sprites/char_ember.png').convert()
char_ember=pygame.transform.scale2x(char_ember)
char_ember_rect=char_ember.get_rect(center=(1140,575))
char_emberb=Button(char_ember,(1003,549))
#INFERNO
char_inferno=pygame.image.load('sprites/char_inferno.png').convert()
char_inferno=pygame.transform.scale2x(char_inferno)
char_inferno_rect=char_inferno.get_rect(center=(1140,630))
char_infernob=Button(char_inferno,(1002,604))
#ROOST
char_roost=pygame.image.load('sprites/char_roost.png').convert()
char_roost=pygame.transform.scale2x(char_roost)
char_roost_rect=char_roost.get_rect(center=(1140,685))
char_roostb=Button(char_roost,(1003,659))
### SQUIRTLE
#PRZOD
squirt_przod=pygame.image.load('sprites/squirtleP.png').convert_alpha()
squirt_przod=pygame.transform.scale2x(squirt_przod)
squirt_przod=pygame.transform.scale2x(squirt_przod)
#TYL
squirt_tyl=pygame.image.load('sprites/squirtleB.png').convert_alpha()
squirt_tyl=pygame.transform.scale2x(squirt_tyl)
squirt_tyl=pygame.transform.scale2x(squirt_tyl)
squirt_tyl=pygame.transform.scale2x(squirt_tyl)
#TACKLE
squirt_tackle=pygame.image.load('sprites/squirt_tackle.png')
squirt_tackle=pygame.transform.scale2x(squirt_tackle)
squirt_tackle_rect=squirt_tackle.get_rect(center=(1140,520))
squirt_tackleb=Button(squirt_tackle,(1003,494))
# WATER PULSE
squirt_water=pygame.image.load('sprites/squirt_water.png')
squirt_water=pygame.transform.scale2x(squirt_water)
squirt_water_rect=squirt_water.get_rect(center=(1140,575))
squirt_waterb=Button(squirt_water,(1003,549))
#DRAIN PUNCH
squirt_drain=pygame.image.load('sprites/squirt_drain.png')
squirt_drain=pygame.transform.scale2x(squirt_drain)
squirt_drain_rect=squirt_drain.get_rect(center=(1140,630))
squirt_drainb=Button(squirt_drain,(1003,604))
#REVENGE
squirt_revenge=pygame.image.load('sprites/squirt_reve.png')
squirt_revenge=pygame.transform.scale2x(squirt_revenge)
squirt_revenge_rect=squirt_revenge.get_rect(center=(1140,685))
squirt_revengeb=Button(squirt_revenge,(1003,661))
### CATERPIE ####
cater=pygame.image.load('sprites/caterpie.png').convert_alpha()
cater=pygame.transform.scale2x(cater)
cater=pygame.transform.scale2x(cater)
### TORKOAL #####
tork=pygame.image.load('sprites/torkoal.png').convert_alpha()
tork=pygame.transform.scale2x(tork)
tork=pygame.transform.scale2x(tork)
### MAGIKARP #####
magi=pygame.image.load('sprites/magikarp.png').convert_alpha()
magi=pygame.transform.scale2x(magi)
magi=pygame.transform.scale2x(magi)
#####WYBOR POKEMONA
scena=pygame.image.load('sprites/bg.png')
pokeball1=pygame.image.load('sprites/ball1.png')
p1=pokeball1.get_rect(topleft=((425, 325)))
pok1=Button(pokeball1,(425,325))
pokeball2=pygame.image.load('sprites/ball2.png')
p2=pokeball2.get_rect(topleft=((575, 350)))
pok2=Button(pokeball2,(575, 350))
pokeball3=pygame.image.load('sprites/ball3.png')
p3=pokeball3.get_rect(topleft=(725, 325))
pok3=Button(pokeball3,(725, 325))
#p1 = screen.blit(pokeball1, (425, 325))
#p2 = screen.blit(pokeball2, (575, 350))
#p3 = screen.blit(pokeball3, (725, 325))
#### PROFESSOR
sycamore=pygame.image.load('sprites/sycamore.png')
sycamore=pygame.transform.scale(sycamore,(448,710))
sycamore=pygame.transform.flip(sycamore,True,False)
####
#####AUDIO
start_music=pygame.mixer.Sound('audio/opening.mp3')
start_music.set_volume(0.05)
battle_music=pygame.mixer.Sound('audio/battle.mp3')
battle_music.set_volume(0.05)
wybor_music=pygame.mixer.Sound('audio/wybor.mp3')
wybor_music.set_volume(0.07)
b_music=pygame.mixer.Sound('audio/bulbasaur.mp3')
b_music.set_volume(0.07)
c_music=pygame.mixer.Sound('audio/charmander.mp3')
c_music.set_volume(0.07)
s_music=pygame.mixer.Sound('audio/squirtle.mp3')
s_music.set_volume(0.07)
ca_music=pygame.mixer.Sound('audio/caterpie.mp3')
ca_music.set_volume(0.07)
m_music=pygame.mixer.Sound('audio/magikarp.mp3')
m_music.set_volume(0.07)
t_music=pygame.mixer.Sound('audio/torkoal.mp3')
t_music.set_volume(0.07)
end_music=pygame.mixer.Sound('audio/end.mp3')
end_music.set_volume(0.05)
pokecenter_music=pygame.mixer.Sound('audio/pokecenter.mp3')
pokecenter_music.set_volume(0.07)
##############
player=wybor_pokemona()
ac=0
runda=1
przeciwnik=0
atak=0
clock=pygame.time.Clock()
dzwignia=False
gra=True
start=True
############################ KOD GŁÓWNY ########################################
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos=pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if ac<2:
                    ac+=1
                elif ac==2:
                    ac=2

    pygame.display.update()
    clock.tick(60)
    #TŁO
    screen.blit(bg_surface, (0, 0))

    if gra:
        pokecenter_music.stop()
        if player==None and start==True:
            screen.blit(start_surface,(0,0))
            start_music.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_music.stop()
                    ac=0
                    start=False
        # WYBOR POKEMONA
        if player==None and start==False:
            wybor_pokemona_display()
            wybor_music.play()
            player=wybor_pokemona()
            przeciwnik_wybrany = False
            ac=0
        # GRATULOWANIE WYBORU
        if player!=None  and ac==0:
            gratulowanie_wyboru(player)
            typ_playera=player.typ
        if player!=None and player.is_alive==True:
            czy_walka=True
        # WYBOR PRZECIWNIKA
            if player!=None and przeciwnik_wybrany==False:
                przeciwnik = przypisanie_przeciwnika()
                typ_przeciwnika=przeciwnik.typ
                przeciwnik_wybrany=True
                # EKRAN PRZED WALKA
            if player!=None and ac==1 and przeciwnik_wybrany==True:
                wybor_music.stop()
                ekran_przed_walka(runda,przeciwnik)
                if przeciwnik.name=='Bulbasaur':
                    b_music.play()
                elif przeciwnik.name=='Charmander':
                    c_music.play()
                elif przeciwnik.name=='Squirtle':
                    s_music.play()
                elif przeciwnik.name=='Caterpie':
                    ca_music.play()
                elif przeciwnik.name=='Magikarp':
                    m_music.play()
                elif przeciwnik.name=='Torkoal':
                    t_music.play()
                if ac==2:
                    czy_ac=True
            if player!=None and ac==2 and czy_walka==True:
                if przeciwnik.name=='Bulbasaur':
                    b_music.stop()
                elif przeciwnik.name=='Charmander':
                    c_music.stop()
                elif przeciwnik.name=='Squirtle':
                    s_music.stop()
                elif przeciwnik.name=='Caterpie':
                    ca_music.stop()
                elif przeciwnik.name=='Magikarp':
                    m_music.stop()
                elif przeciwnik.name=='Torkoal':
                    t_music.stop()
                battle_music.play()
                display_walka(player,przeciwnik)
                czy_walka=walka(player,przeciwnik,typ_playera,typ_przeciwnika)
                if czy_walka==False and przeciwnik.is_alive==False:
                    battle_music.stop()
                    przeciwnik_wybrany=False
                    ac=1
                    runda+=1
        elif player!=None and player.is_alive==False:
            battle_music.stop()
            pokecenter_music.play()
            ekran=porazka(runda, przeciwnik, player)
            if ekran==True:
                player=None
                ac=0
                runda=1
                start=True
            elif ekran==False:
                gra=False
    elif gra==False:
        pokecenter_music.stop()
        end_music.play()
        screen.blit(end_surface, (0, 0))
pygame.quit()