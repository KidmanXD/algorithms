import pytest
from cards.deck import Card
from cards.black_jack import Player, BlackJack, Simulation

@pytest.fixture
def player():
    return Player()

@pytest.fixture
def blackjack():
    return BlackJack()

@pytest.fixture
def simulation():
    return Simulation()

def test_add_card(player):
    card = Card("A", "hearts", 11, 1)
    player.add(card)
    assert player.score == 11

def test_add_exceeded_card(player):
    with pytest.raises(ValueError):
        card1 = Card("K", "hearts", 10, 0)
        card2 = Card("Q", "hearts", 10, 0)
        card3 = Card("J", "hearts", 10, 0)
        player.add(card1)
        player.add(card2)
        player.add(card3)

def test_step_card(blackjack):
    card = blackjack.step()
    assert isinstance(card, Card)

def test_reset_deck(blackjack):
    deck1 = blackjack.deck
    blackjack.reset()
    deck2 = blackjack.deck
    assert deck1 != deck2