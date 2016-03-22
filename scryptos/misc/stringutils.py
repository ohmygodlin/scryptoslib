from scryptos.util.hexutil import hex

class StreamReader:
  def __init__(s, x):
    s.str = x
    s.pos = 0

  def read(s, length=1):
    if (s.pos + length) > len(s.str):
      length = len(s.str) - s.pos
    res = s.str[s.pos:s.pos+length]
    s.pos += length
    return res

  def seek(s, pos):
    assert 0 <= pos < len(s.str)
    s.pos = pos

  def len(s):
    return len(s.str)

  def __len__(s):
    return s.len()

def xorstr(s, key):
  out = ""
  if type(key) is int:
    key = hex(key, 2)[2:].decode("hex")
  for x in xrange(len(s)):
    out += chr(ord(s[x]) ^ ord(key[x % len(key)]))
  return out

def mapstr(s, t, func):
  out = ""
  for x in xrange(len(s)):
    out += chr(func(s[x]), x)
  return out

def transpose(s):
  return "".join(map(lambda x: "".join(x), zip(*s)))

def nth_split(s, n):
  r = []
  i = 0
  while True:
    if i + n > len(s):
      r += [s[i:]]
      break
    r += [s[i:i+n]]
    i += n
  if r[-1] == "":
    r = r[:-1]
  return r

