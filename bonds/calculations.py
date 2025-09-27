import QuantLib as ql
from .models import Bond

today = ql.Date.todaysDate()
calendar = ql.Poland()
today = calendar.advance(today, ql.Period(2, ql.Days), ql.Following, True)


def create_fixed_bond(bond: Bond, settlement_date: ql.Date = today):

    bond_schedule = ql.Schedule(
        ql.Date(bond.issue_date.day, bond.issue_date.month, bond.issue_date.year),
        ql.Date(bond.maturity_date.day, bond.maturity_date.month, bond.maturity_date.year),
        ql.Period(ql.Annual),
        ql.Poland(),
        ql.Following,
        ql.Following,
        ql.DateGeneration.Backward,
        False
    )

    bond = ql.FixedRateBond(
        2,
        100.0,
        bond_schedule,
        [0.025],
        # [float(bond.coupon_rate/100)],
        ql.ActualActual(ql.ActualActual.ISDA),
        ql.Following,
        100.0,
        ql.Date(bond.issue_date.day, bond.issue_date.month, bond.issue_date.year)
    )

    ql.Settings.instance().evaluationDate = settlement_date
    flat_curve = ql.YieldTermStructureHandle(ql.FlatForward(today,
                                                            0.025,
                                                            ql.Actual365Fixed(),
                                                            ql.Annual))
    bond_engine = ql.DiscountingBondEngine(flat_curve)
    bond.setPricingEngine(bond_engine)

    bond = { 'dirtyPrice': bond.dirtyPrice(),
             'cleanPrice': bond.cleanPrice(),
             'accruedAmount': bond.accruedAmount(),
             'duration': ql.BondFunctions.duration(bond, 0.025,
                                                   ql.ActualActual(ql.ActualActual.Bond),
                                                   ql.Annual,
                                                   1),
             }
    return bond

def describe_day(today_date: ql.Date):
    context ={
        'today_date': today_date,
        'today_date_iso': today_date.ISO(),
        'today_weekday': today_date.weekday()
    }
    return context

