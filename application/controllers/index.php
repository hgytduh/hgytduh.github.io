<?php
	if (!defined('BASEPATH'))
	exit('No direct script access allowed');
	  
	class index extends CI_Controller {
			// Hàm khởi tạo
		function __construct() {
			// Gọi đến hàm khởi tạo của cha
			parent::__construct();
			//$this->load->library("database");
		}
		public function index() {
			$this->load->database();
			$this->load->model('var_model');
			$var = $this->var_model->get_var();
			
			
			
			$this->db->select("name,value");
			$query=$this->db->get("var");
			$rs=$query->result_array();
			$n=$query-> num_rows();
			$data_menu = array();
			for($i=0;$i<$n;$i++){
				$data_menu[$rs[$i]['name']] = $rs[$i]['value'];
			}
			
			
			
			
			
			
			
			
			
			$menu = $this->load->view('menu_view',$data_menu,true);
			$data = array(
			'menu'=>$menu
			);
			$this->load->view('index_view',$data);
		}
	}
?>