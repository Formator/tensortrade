
from tensortrade.env.generic import Stopper, TradingEnv


class MaxLossStopper(Stopper):
    """A stopper that stops an episode if the portfolio has lost a particular
    percentage of its wealth.

    Parameters
    ----------
    max_allowed_loss : float
        The maximum proportion of initial funds that is willing to
        be lost before stopping the episode.

    Attributes
    ----------
    max_allowed_loss : float
        The maximum proportion of initial funds that is willing to
        be lost before stopping the episode.

    Notes
    -----
    This stopper also stops if it has reached the end of the observation feed.
    """

    def __init__(self, max_allowed_loss: float):
        super().__init__()
        self.max_allowed_loss = max_allowed_loss

    def stop(self, env: 'TradingEnv') -> bool:
        c1 = env.action_scheme.portfolio.profit_loss < self.max_allowed_loss
        print(env.action_scheme.portfolio.profit_loss)
        print("c1 = {}".format(c1))
        c2 = not env.observer.has_next()
        print("c2 = {}".format(c2))
        return c1 or c2
