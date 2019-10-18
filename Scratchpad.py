class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = Message(text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        for i in range(27):
            self.best_shift = (0,self.message_text.apply_shift(26-i))
            self.decrypted_message = self.message_text.apply_shift(26-i)
            self.sentLen = len(self.decrypted_message.split(' '))
            #print(self.decrypted_message)
            c = 0
            for j in self.decrypted_message.split(' '):
                c += 1
                #print(j, c)
                if is_word(self.valid_words, j) == True:
                    if c == self.sentLen:
                        self.best_shift = (i,self.decrypted_message)
                        return self.best_shift
                    else:
                        pass
                else:
                    pass
        return self.best_shift