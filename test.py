from ProviderRepository import providerRepository

provider = providerRepository()

card1 = provider.card('1',"S")
card1.print_card()
card2 = provider.card('5',"H")
card2.print_card()