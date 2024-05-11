# Sometimes, it feels like we're launching a spacecraft when all we want to do is say "Hello, World!".


class Greeter:

  def __init__(self, greeting):
    self.greeting = greeting

  def greet(self):
    print(self.greeting)


def main():
  greeter = Greeter("Hello, World!")
  greeter.greet()


if __name__ == "__main__":
  main()
