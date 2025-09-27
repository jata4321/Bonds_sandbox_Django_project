import QuantLib as ql

# Date Parameters
evaluation_date = ql.Date(26, 9, 2025)
today_date = ql.Date.todaysDate()

ql.Settings.evaluationDate = evaluation_date

# Bond Parameters
issue_date = ql.Date(23, 4, 2025)
maturity_date = ql.Date(25, 7, 2030)
coupon_rate = 0.045
coupons = [coupon_rate]
face_value = 100

# Conventions and Calendars
day_count_convention = ql.ActualActual(ql.ActualActual.Actual365) # counting days between dates (accruals)
calendar = ql.Poland()
settlement_days = 2
settlement_date = calendar.advance(evaluation_date, settlement_days, ql.Days)
business_day_convention = ql.ModifiedFollowing  # coupon payment if not in business day
compounding_scheme = ql.Compounded
frequency = ql.Annual
tenor = ql.Period(frequency)

schedule = ql.Schedule(
    issue_date,
    maturity_date,
    tenor,
    calendar,
    business_day_convention,
    business_day_convention,
    ql.DateGeneration.Backward,
    False
)

print(list(schedule.dates()))

bond = ql.FixedRateBond(
    settlement_days,
    face_value,
    schedule,
    coupons,
    day_count_convention,
    business_day_convention
)

spot_curve = ql.FlatForward(0,
                            calendar,
                            ql.QuoteHandle(ql.SimpleQuote(0.03889)),
                            ql.ActualActual(ql.ActualActual.Bond),
                            compounding_scheme,
                            frequency)
discount_curve = ql.RelinkableYieldTermStructureHandle(spot_curve)
engine = ql.DiscountingBondEngine(discount_curve)

bond.setPricingEngine(engine)

print('NPV:', bond.NPV())
print('Clean price:', bond.cleanPrice())
print('Dirty price:', bond.dirtyPrice())
print('Accrued Int:', bond.accruedAmount())

market_clean_price = 98.37384
bond_price = ql.BondPrice(market_clean_price, ql.BondPrice.Clean)

ytm = ql.BondFunctions.bondYield(
    bond,
    bond_price,
    day_count_convention,
    compounding_scheme,
    frequency,
)
print('Ytm: ', ytm)

mac_duration = ql.BondFunctions.duration(
    bond,
    ytm,
    day_count_convention,
    compounding_scheme,
    frequency,
    ql.Duration.Macaulay
)
print('Duration: ', mac_duration)

mod_duration = ql.BondFunctions.duration(
    bond,
    ytm,
    day_count_convention,
    compounding_scheme,
    frequency,
    ql.Duration.Modified
)
print('Modified Duration: ', mod_duration)

convexity = ql.BondFunctions.convexity(
    bond,
    ytm,
    day_count_convention,
    compounding_scheme,
    frequency,
)
print('Convexity: ', convexity)
