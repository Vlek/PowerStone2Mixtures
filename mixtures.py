"""
One thing that could cause problems are circular combinations. In
order to ensure that that does not cause a recursion issue, we should
first check whether the new price is any better than the old one for
a given item. If it is worse or the same, then we do not need to
propagate the price to other items.

This structure allows for combinations of any number of items and
outputs. That would simply change how many items register that they
will need to recompute downstream items.

One could also incorporate the ability to update the price of a given
item, and have that cause the ripple effects through the combinations
as that structure would have already been saved. This would allow for
the prices to be updated over time without having to change the prices
and recreate the structure each time.
"""

from models import Item






if __name__ == "__main__":
    for combo in COMBINATIONS:
        ITEMS[combo[0]].addDependentCombination(combo)
        ITEMS[combo[1]].addDependentCombination(combo)

    for item in ITEMS:
        print(ITEMS[item])
