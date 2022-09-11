# Test-driven Development on _Speed_


## Requirements

1. Bus accepts passengers
2. Bus can accelerate $v_0 \to v_1$ mph, where $v_1 > v_0$
3. Bus can decelerate from $v_1 \to v_2$, where $v_2 < v_1$
4. There is an unarmed bomb on the bus!
5. When the bomb is unarmed **and** the bus accelerates to $v \geq 50$ mph, the bomb is armed
6. When the bomb is armed **and** the bus decelerates to $v \leq 50$, the bomb explodes **unless** there is at least one passenger on the bus who can save the day (go Keanu!)
