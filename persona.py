class Persona:
    def greet(self, name: str = 'estudiante') -> None:
        print('Hola {}!'.format(name))

pablo = Persona()

pablo.greet('Jaime')
pablo.greet('Chavo')
