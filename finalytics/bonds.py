def bond_price(
    face_value,
    coupon_rate,
    yield_rate,
    years,
    payments_per_year=1,
):

    n = int(years * payments_per_year)
    c = face_value * coupon_rate / payments_per_year
    y = yield_rate / payments_per_year

    cashflows = [c] * n
    cashflows[-1] += face_value

    price = 0.0
    for t, cf in enumerate(cashflows, start=1):
        price += cf / ((1 + y) ** t)
    return price


def yield_to_maturity(
    price,
    face_value,
    coupon_rate,
    years,
    payments_per_year=1,
    guess_low=0.0,
    guess_high=1.0,
    tol=1e-6,
    max_iter=1000,
):

    def price_for_yield(yield_rate: float):
        return bond_price(face_value, coupon_rate, yield_rate, years, payments_per_year)

    low, high = guess_low, guess_high
    p_low = price_for_yield(low)
    p_high = price_for_yield(high)

    f_low = p_low - price
    f_high = p_high - price

    if f_low * f_high > 0:
        raise ValueError(
            "YTM search interval does not bracket a root. "
            "Try different guess_low/guess_high."
        )

    for _ in range(max_iter):
        mid = (low + high) / 2.0
        p_mid = price_for_yield(mid)
        f_mid = p_mid - price

        if abs(f_mid) < tol:
            return mid

        if f_low * f_mid < 0:
            high = mid
            f_high = f_mid
        else:
            low = mid
            f_low = f_mid

    return (low + high) / 2.0


def _bond_cashflows(face_value, coupon_rate, years, payments_per_year):
    n = int(years * payments_per_year)
    c = face_value * coupon_rate / payments_per_year
    cfs = [c] * n
    cfs[-1] += face_value
    return cfs


def duration(
    face_value,
    coupon_rate,
    yield_rate,
    years,
    payments_per_year=1,
):

    n = int(years * payments_per_year)
    y = yield_rate / payments_per_year
    cfs = _bond_cashflows(face_value, coupon_rate, years, payments_per_year)

    price = 0.0
    weighted_sum = 0.0
    for t, cf in enumerate(cfs, start=1):
        pv = cf / ((1 + y) ** t)
        price += pv
        weighted_sum += t * pv

    if price == 0:
        return 0.0

    D_periods = weighted_sum / price
    return D_periods / payments_per_year


def modified_duration(
    face_value,
    coupon_rate,
    yield_rate,
    years,
    payments_per_year=1,
):

    D = duration(face_value, coupon_rate, yield_rate, years, payments_per_year)
    y = yield_rate / payments_per_year
    return D / (1 + y)


def convexity(
    face_value,
    coupon_rate,
    yield_rate,
    years,
    payments_per_year=1,
):

    n = int(years * payments_per_year)
    y = yield_rate / payments_per_year
    m = payments_per_year
    cfs = _bond_cashflows(face_value, coupon_rate, years, payments_per_year)

    price = 0.0
    conv_sum = 0.0
    for t, cf in enumerate(cfs, start=1):
        discount = (1 + y) ** t
        pv = cf / discount
        price += pv
        conv_sum += cf * t * (t + 1) / ((1 + y) ** (t + 2))

    if price == 0:
        return 0.0

    return conv_sum / price / (m**2)
