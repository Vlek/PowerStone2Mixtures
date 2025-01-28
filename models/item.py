class Item:
    def __init__(
            self, name: str, itemId: str, level: int, sellPrice: int, buyPrice: int, requiresText: bool
    ) -> None:
        self.name: str = name
        self.itemId: str = itemId
        self.level: int = level
        self.sellPrice: int = sellPrice
        self.buyPrice: int = buyPrice
        self.requiresText: bool = requiresText

        self.lowestCost: list = []

        if self.buyPrice is not None:
            self.lowestCost = [self.buyPrice, "buy"]

        # Here is where the magic happens. When we incorporate new combination
        # possibilities, then we are going to calculate the new cost of those
        # items based on the cost of their components.
        #
        # The structure is item1, item2, and the output.
        self.dependentCombinations: list[list[str]] = []

    def recalculateDependentCombinations(self) -> None:
        for combo in self.dependentCombinations:
            self.calculateCombination(combo)

    def calculateCombination(self, combination: list[str]) -> None:
        item1: Item = ITEMS[combination[0]]
        item2: Item = ITEMS[combination[1]]

        if len(item1.lowestCost) == 0 or len(item2.lowestCost) == 0:
            return

        newCost: int = (
            ITEMS[combination[0]].lowestCost[0] + ITEMS[combination[1]].lowestCost[0]
        )

        if (
            len(ITEMS[combination[2]].lowestCost) == 0
            or newCost < ITEMS[combination[2]].lowestCost[0]
        ):
            ITEMS[combination[2]].changeLowestCost(
                [newCost, "mix", ITEMS[combination[0]], ITEMS[combination[1]]]
            )

    def addDependentCombination(self, combination: list[str]) -> None:
        self.dependentCombinations.append(combination)

        self.calculateCombination(combination)

    def changeLowestCost(self, cost: list) -> None:
        self.lowestCost = cost

        self.recalculateDependentCombinations()

    def __str__(self) -> str:
        bestIngredients: str = ""
        if len(self.lowestCost) != 0:
            if self.lowestCost[1] == "mix":
                bestIngredients = (
                    f"mix: {self.lowestCost[2].name} and {self.lowestCost[3].name}"
                )
            else:
                bestIngredients = f"buy for {self.lowestCost[0]}"
        else:
            bestIngredients = "No mixture, cannot buy"

        return f"{self.name}: {('n/a' if len(self.lowestCost) == 0 else self.sellPrice - self.lowestCost[0])} {bestIngredients}"
