class __Interactive:
    '''Creates a generic interactive'''
    def __init__(self,base:pygame.Surface):
        self.sprite = base                                             # Surface of the button
        self.rect = None
        self.pos = (0,0)                                               # top-left corner

    def position(self,pos:tuple):
        pos = (pos[1],pos[0])
        self.rect = self.sprite.get_rect(center=pos)
        self.pos = self.rect.topleft

    def draw(self,screen):
        screen.blit(self.sprite, self.pos)

class _Selection(__Interactive):
    '''A simple on/off switch'''
    def __init__(self, base: pygame.Surface, check: pygame.Surface, action = None, status: bool = False):
        super().__init__(base)
        self.check = check                                          # Surface for the checkmark
        self.checkpos = (0,0)
        self.status = status                                        # checked/not
        self.action = action

    def position(self,pos:tuple):
        pos = (pos[1],pos[0])
        self.rect = self.sprite.get_rect(center=pos)
        self.pos = self.rect.topleft
        self.checkpos = self.check.get_rect(center=self.rect.center).topleft

    def select(self):
        Settings.writing = False
        self.status = self.status == False
        if self.action!=None:
            self.action()
    
    def draw(self,screen):
        screen.blit(self.sprite, self.pos)
        if self.status:
            screen.blit(self.check, self.checkpos)

class _Button(__Interactive):
    '''A clickable button'''
    def __init__(self, base: pygame.Surface, action):
        super().__init__(base)
        self.action = action
    
    def select(self):
        Settings.writing = False
        self.action()

class _TextInput(_Button):
    '''A text box'''
    def __init__(self, base: pygame.Surface, action, variable:int='write here'):
        super().__init__(base, self._on_click)
        self.FONT = Settings.FONT
        self.value = variable
    
    def _on_click(self):
        if not Settings.writing:
            self.sprite = self.FONT.render(str(self.value), True, (128,128,128), (0,0,0))
            Settings.writing = True

    def on_key_press(self, key) -> int:
        pass
