//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for pb_type: fle
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Physical programmable logic block Verilog module: fle -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_clb_mode_default__fle -----
module logical_tile_clb_mode_default__fle(reset,
                                          clk,
                                          fle_in,
                                          fle_clk,
                                          bl,
                                          wl,
                                          fle_out);
//----- GLOBAL PORTS -----
input [0:0] reset;
//----- GLOBAL PORTS -----
input [0:0] clk;
//----- INPUT PORTS -----
input [0:5] fle_in;
//----- INPUT PORTS -----
input [0:0] fle_clk;
//----- INPUT PORTS -----
input [0:65] bl;
//----- INPUT PORTS -----
input [0:65] wl;
//----- OUTPUT PORTS -----
output [0:0] fle_out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_clb_mode_default__fle_mode_physical__ble6 logical_tile_clb_mode_default__fle_mode_physical__ble6_0 (
		.reset(reset),
		.clk(clk),
		.ble6_in({direct_interc_1_out, direct_interc_2_out, direct_interc_3_out, direct_interc_4_out, direct_interc_5_out, direct_interc_6_out}),
		.ble6_clk(direct_interc_7_out),
		.bl(bl[0:65]),
		.wl(wl[0:65]),
		.ble6_out(logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out));

	direct_interc direct_interc_0_ (
		.in(logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out),
		.out(fle_out));

	direct_interc direct_interc_1_ (
		.in(fle_in[0]),
		.out(direct_interc_1_out));

	direct_interc direct_interc_2_ (
		.in(fle_in[1]),
		.out(direct_interc_2_out));

	direct_interc direct_interc_3_ (
		.in(fle_in[2]),
		.out(direct_interc_3_out));

	direct_interc direct_interc_4_ (
		.in(fle_in[3]),
		.out(direct_interc_4_out));

	direct_interc direct_interc_5_ (
		.in(fle_in[4]),
		.out(direct_interc_5_out));

	direct_interc direct_interc_6_ (
		.in(fle_in[5]),
		.out(direct_interc_6_out));

	direct_interc direct_interc_7_ (
		.in(fle_clk),
		.out(direct_interc_7_out));

endmodule
// ----- END Verilog module for logical_tile_clb_mode_default__fle -----

//----- Default net type -----
// `default_nettype none



// ----- END Physical programmable logic block Verilog module: fle -----
