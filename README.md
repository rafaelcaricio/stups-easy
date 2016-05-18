# STUPS Easy
Easy to never forget STUPS commands.
![Dory](https://2.bp.blogspot.com/-DggOtQetGGg/UZp03H7JYxI/AAAAAAAAABM/MnO_ekSbugk/s1600/dory.jpg)

## Porpose

STUPS Easy is a tool to break the berrier for newbies of getting to
know each of the command line tools necessary to use STUPS
infrastructure. You call the `easy` tool with mnemonic subcommands
that will get translated to the proper STUPS command line tool you
need for that particular task. Also it shows you the actual command
using the STUPS tool directly so at some point you will be familiar
with the tools you most use and can start using it directly.

## How to install

``` shell
$ git clone git@github.bus.zalan.do:rcaricio/stups-easy.git
$ cd stups-easy
$ python3 setup.py install
```

## Usage

STUPS Easy is a tool to help you remember stups commands easily.

``` shell
$ easy artifacts list bus
```

Available subcommands that translates to STUPS tools:

 - `login`: Use
   [`mai`](http://stups.readthedocs.io/en/latest/components/mai.html)
   command line utility to retrieve temporary AWS credentials.
 - `deploy`: Use
   [`senza`](http://stups.readthedocs.io/en/latest/components/senza.html)
   deployment tool.
 - `artifacts`: Use
   [`pierone`](http://stups.readthedocs.io/en/latest/components/pierone.html)
   artifact store command line tool.
 - `ssh`: Use
   [`piu`](http://stups.readthedocs.io/en/latest/components/piu.html)
   SSH access granting service.
 - `compliance`: Use
   [`fullstop`](https://docs.stups.io/en/latest/components/fullstop.html)
   command line tool for managing violations across all AWS accounts.
 - `versions`: Use
   [`kio`](https://docs.stups.io/en/latest/components/kio.html)
   application registry for managing versions.

All subcommands arguments are passed to the subcommands directly so
you do not need to wait for STUPS Easy to get updated to use something
new in the original command line STUPS tools.
