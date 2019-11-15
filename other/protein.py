import csv
from PyBioMed.PyProtein import AAComposition

protein="CGQGFSVKSDVITHQRTHTGEKLYVCRECGRGFSWKSHLLIHQRIHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSNKSHLLRHQRTHTGEKPYVCRECGRGFRDKSHLLSHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFSWQSVLLRHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFRNKSHLLRHQRTHTGEKPYVCRECGRGFSDRSSLCYHQRTHTGEKPYVCREDE"

protein2="MAAAKAEMQLMSPLQISDPFGSFPHSPTMDNYPKLEEMMLLSNGAPQFLGAAGTPEGSGGNSSSSTSSGGGGGGGSNSGSSAFNPQGEPSEQPYEHLTTESFSDIALNNEKAMVETSYPSQTTRLPPITYTGRFSLEPAPNSGNTLWPEPLFSLVSGLVSMTNPPTSSSSAPSPAASSSSSASQSPPLSCAVPSNDSSPIYSAAPTFPTPNTDIFPEPQSQAFPGSAGTALQYPPPAYPATKGGFQVPMIPDYLFPQQQGDLSLGTPDQKPFQGLENRTQQPSLTPLSTIKAFATQSGSQDLKALNTTYQSQLIKPSRMRKYPNRPSKTPPHERPYACPVESCDRRFSRSDELTRHIRIHTGQKPFQCRICMRNFSRSDHLTTHIRTHTGEKPFACDICGRKFARSDERKRHTKIHLRQKDKKADKSVVASPAASSLSSYPSPVATSYPSPATTSFPSPVPTSYSSPGSSTYPSPAHSGFPSPSVATTFASVPPAFPTQVSSFPSAGVSSSFSTSTGLSDMTATFSPRTIEIC"

AAC=AAComposition.CalculateAAComposition(protein)

AAC2=AAComposition.CalculateAAComposition(protein2)

print type(AAC)

print AAC

with open('keys.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(AAC.values())

with open('keys.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(AAC2.values())

# with open('test.csv', 'wb') as f:
#     writer = csv.writer(f)
#     for row in AAC.iteritems():
#         writer.writerow(row)