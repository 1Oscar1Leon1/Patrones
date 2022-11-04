from __future__ import annotations
class Facade:
    def __init__(self, sub_system1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()
    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_a())
        results.append(self._subsystem2.operation_b())
        return "\n".join(results)
class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: _Active_"
    def operation_a(self) -> str:
        return "Subsystem1: _Ready_"
class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: _Ready_"
    def operation_b(self) -> str:
        return "Subsystem2: _Danger!_"
def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")
if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)