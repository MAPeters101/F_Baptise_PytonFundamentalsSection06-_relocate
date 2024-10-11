open_, high, low, close = 98, 100, 95, 99

print('open: ' + str(open_) + ', high: ' + str(high) + ', low: ' + str(low) + ', close: ' + str(close))
print('open: {}, high: {}, low: {}, close: {}'.format(open_, high, low, close))
#print('open: {}, high: {}, low: {}, close: {}'.format(open_, high, low))
print('open: {}, high: {}, low: {}, close: {}'.format(open_, high, low, 100))
print(f'open: {open_}, high: {high}, low: {low}, close: {close}')

bid = 1.5760
ask = 1.5763

print('bid: {}, ask {}, spread: {}'.format(bid, ask, ask-bid))
print(f'bid: {bid}, ask {ask}, spread: {ask-bid}')
print('bid: {b}, ask {a}, spread: {spread}'.format(a=ask, b=bid, spread=ask-bid))

print(format(0.1, '.10f'))

print('bid: {:.4f}, ask {:.4f}, spread: {:.4f}'.format(bid, ask, ask-bid))
print(f'bid: {bid:.4f}, ask {ask:.4f}, spread: {ask-bid:.4f}')
print(f'bid: {bid:.4f}, ask {ask:.4f}, spread: {(ask-bid):.4f}')
print('bid: {b:.4f}, ask {a:.4f}, spread: {spread:.4f}'.format(a=ask, b=bid, spread=ask-bid))


