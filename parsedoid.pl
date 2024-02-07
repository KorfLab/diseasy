use strict;
use warnings;

my $genetic = '0050735|0050736|0050737|0050738|0050739';

my %found;
while (<>) {
	chomp;
	next unless /^(\w+): (.+)/;
	$found{$1} = $2;
	next unless $1 eq 'is_a' and $_ =~ /$genetic/;
	if ($found{'def'} =~ /gene/) {
		#print $found{'def'}, "\n";
		if ($found{'def'} =~ /([A-Z]{2,}[A-Z0-9]+) gene/) {
			print "$1\n";
		} elsif ($found{'def'} =~ /gene \(([A-Z]{2,}[A-Z0-9]+)\)/) {
			print "$1\n";
		}
	}
	
	#next unless $found{'def'} =~ / gene[^s]/;
	#print join("\t", $found{'name'}, $found{'def'}), "\n\n";
}


__END__
is_a: DOID:0050735 ! X-linked monogenic disease
is_a: DOID:0050736 ! autosomal dominant disease
is_a: DOID:0050737 ! autosomal recessive disease
is_a: DOID:0050738 ! Y-linked monogenic disease
is_a: DOID:0050739 ! autosomal genetic disease
