#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Auto Scan
# Generated: Fri Aug  4 23:19:59 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import iio
import wx, time, sys


class auto_scan(grc_wxgui.top_block_gui):

    def __init__(self, freq=325000000, outfile='./output.wav'):
        grc_wxgui.top_block_gui.__init__(self, title="Auto Scan")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.outfile = outfile

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2**22
        self.bandwidth = bandwidth = 20000000

        ##################################################
        # Blocks
        ##################################################
        self.pluto_source_0 = iio.pluto_source('', freq, samp_rate, 1 - 1, bandwidth, 0x8000, True, True, True, "manual", 64.0, '', True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, outfile, True)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.pluto_source_0, 0), (self.blocks_file_sink_0, 0))    

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.pluto_source_0.set_params(self.freq, self.samp_rate, self.bandwidth, True, True, True, "manual", 64.0, '', True)

    def get_outfile(self):
        return self.outfile

    def set_outfile(self, outfile):
        self.outfile = outfile
        self.blocks_file_sink_0.open(self.outfile)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.pluto_source_0.set_params(self.freq, self.samp_rate, self.bandwidth, True, True, True, "manual", 64.0, '', True)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.pluto_source_0.set_params(self.freq, self.samp_rate, self.bandwidth, True, True, True, "manual", 64.0, '', True)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-f", "--freq", dest="freq", type="intx", default=325000000,
        help="Set f [default=%default]")
    parser.add_option(
        "-o", "--outfile", dest="outfile", type="string", default='./output.wav',
        help="Set fle [default=%default]")
    return parser


def main(top_block_cls=auto_scan, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(freq=options.freq, outfile=options.outfile)
    tb.Start(True)
    time.sleep(2)
    sys.exit()
    tb.Wait()


if __name__ == '__main__':
    main()
