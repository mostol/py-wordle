import abc


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[str]:  # Just using str as filler for now.
        raise NotImplementedError
