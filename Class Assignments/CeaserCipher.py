"""
Ceaser Cipher program to take a message, the nshow its encryption and decryption
Corey Fults
"""

#class to handle ceaser_cipher functions
class ceaser_cipher:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def init(self):
      print("Ceaser cipher instance created")

    #encrypt a message
    def encrypt(self, key, msg):
      encryption = ""
      for char in msg:
        if char in self.alphabet:
          pos = self.alphabet.find(char)
          encryption += self.alphabet[(pos+key) % len(self.alphabet)]
        else:
          encryption += char
      return encryption

    #decrypt a encrypted message
    def decrypt(self, key, msg):
      decryption = ""
      for char in msg:
        if char in self.alphabet:
          pos = self.alphabet.find(char)
          decryption += self.alphabet[(pos-key) % len(self.alphabet)]
        else:
          decryption += char
      return decryption

#class to hold my input utilities
class input_utils:
  #convert a string/value to bool
  def to_bool(value):
      """
         Converts 'something' to boolean. Raises exception for invalid formats
             Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
             Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
      """
      if str(value).lower() in ("yes", "y", "true",  "t", "1"):
          return True
      if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"):
          return False
      raise Exception('Invalid value for boolean conversion: ' + str(value))

  #grab user input for the cipher key
  def get_key():
    while True:
      try:
        key = int(input("Enter your secret key (Number): "))
        return key
      except ValueError:
        print("Invalid input. Please enter a number.")

  #grab user number input within set bounds
  def get_user_input_num(text, min, max):
      while True:
          user_inp = ""
          try:
              user_inp = input(text)
              amnt = int(user_inp)
              if len(str(amnt)) == 0 or amnt > max or amnt < min:
                  print("Must be a number & between %i-%i" % (min, max))
              else:
                  return amnt
          except ValueError:
              if user_inp == "forcequit":
                  raise SystemExit(0)
              print("Must be a number")

  #grab yes/no input
  def get_yes_no(question, default='no'):
      if default is None:
          prompt = " [y/n] "
      elif default == 'yes':
          prompt = " [Y/n] "
      elif default == 'no':
          prompt = " [y/N] "
      else:
          raise ValueError("Unknown setting '{default}' for default.")

      while True:
          try:
              resp = input(question + prompt).strip().lower()
              if default is not None and resp == '':
                  return default == 'yes'
              else:
                  return input_utils.to_bool(resp)
          except ValueError:
              print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

#core loop
def main():
  cipher = ceaser_cipher()
  while True:
    key = input_utils.get_key()
    message = input("Enter your message to encrypt: ").lower()

    encrypted_msg = cipher.encrypt(key, message)
    print("Encryption: %s" % encrypted_msg)
    print("Decryption: %s" % cipher.decrypt(key, encrypted_msg))
    option = input_utils.get_yes_no("Encrypt another message?: ", default='no')
    if not option:
      break
  print("Exiting..")


main()
