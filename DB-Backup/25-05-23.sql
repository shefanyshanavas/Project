-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 22, 2023 at 04:44 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cheff`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_tbl`
--

CREATE TABLE `admin_tbl` (
  `admin_id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `passw` varchar(150) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_tbl`
--

INSERT INTO `admin_tbl` (`admin_id`, `user_name`, `email`, `passw`, `created_at`, `status`) VALUES
(1, 'test', 'admin@gmail.com', '3c83751e645721983ba82566ba888881', '2023-05-21 16:16:54', 1),
(2, 'test user', 'admin1@gmail.com', '3c83751e645721983ba82566ba888881', '2023-05-22 14:39:46', 1),
(3, 'test2', 'admin2@gmail.com', '3c83751e645721983ba82566ba888881', '2023-05-22 14:27:57', 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$oXx76pxmprGmIQUUqztpiS$YZQKBy+/qISRvwSGwwf6vDbB6cFiQ7ZDRmtzBciL/+Y=', '2023-05-06 07:59:16.699286', 1, 'savio', '', '', 'savioalwd@gmail.com', 1, 1, '2023-05-06 07:55:36.075430');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bike_brand_tbl`
--

CREATE TABLE `bike_brand_tbl` (
  `brand_id` int(11) NOT NULL,
  `brand_name` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bike_brand_tbl`
--

INSERT INTO `bike_brand_tbl` (`brand_id`, `brand_name`, `created_at`, `status`) VALUES
(4, 'loco', '2023-05-16 05:16:22', 0),
(6, 'BAJAAJ', '2023-05-08 04:39:39', 1),
(7, 'KTM', '2023-05-08 04:39:50', 1),
(8, 'Ducati', '2023-05-10 09:29:50', 1),
(9, 'Pavilo', '2023-05-16 05:16:31', 1);

-- --------------------------------------------------------

--
-- Table structure for table `bike_purchase_tbl`
--

CREATE TABLE `bike_purchase_tbl` (
  `purchase_id` int(11) NOT NULL,
  `bike_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `bill_address` varchar(250) NOT NULL,
  `bill_pincode` varchar(50) NOT NULL,
  `contact_no` varchar(100) NOT NULL,
  `purchase_type` tinyint(1) NOT NULL,
  `aadhar_no` varchar(100) NOT NULL,
  `signature_img` varchar(250) NOT NULL,
  `aadhar_img` varchar(250) NOT NULL,
  `other_proof_img` varchar(250) NOT NULL,
  `expected_delivery` timestamp NULL DEFAULT current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` int(11) NOT NULL,
  `bill_name` varchar(100) NOT NULL,
  `payment_status` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bike_purchase_tbl`
--

INSERT INTO `bike_purchase_tbl` (`purchase_id`, `bike_id`, `user_id`, `bill_address`, `bill_pincode`, `contact_no`, `purchase_type`, `aadhar_no`, `signature_img`, `aadhar_img`, `other_proof_img`, `expected_delivery`, `created_at`, `status`, `bill_name`, `payment_status`) VALUES
(25, 10, 11, 'dkjshfkjdshf sdjkfhdskj hfdjshf', '683511', '7012545907', 1, '1245 6598 3265', '65770.png', '2019-Aprilia-Shiver-900.jpg', '80621.jpg', '2023-05-29 07:53:11', '2023-05-14 07:53:11', 2, '683511', 1),
(26, 10, 11, 'jfhgjdhgj fdghdfkj gkjdfkjgkjdf', '683511', '7012545907', 0, '5468 2365 6598', '65770.png', '2019-Aprilia-Shiver-900.jpg', '80621.jpg', '2023-05-29 07:55:09', '2023-05-14 07:55:09', 3, 'sdfsdfdsfdsf', 1),
(27, 10, 10, 'dgfjdfkjg dfkgj dfkljg', '683511', '7012545907', 0, '1245 1245 3561', '20210902155351.jpg', 'electric_bike_1643964192692_1643964202949.jpg', '108080_1389693010.jpg', '2023-05-30 07:51:02', '2023-05-15 07:51:02', 4, 'test', 1),
(29, 10, 10, 'sdfjhdskjhfdkjshfkdskjfkj s', '683511', '7012545907', 1, '8546 8456 2365', '80621.jpg', '65770.png', '2019-Aprilia-Shiver-900.jpg', '2023-05-31 05:57:35', '2023-05-16 05:57:35', 3, 'tsset', 0);

-- --------------------------------------------------------

--
-- Table structure for table `cities`
--

CREATE TABLE `cities` (
  `id` int(11) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`id`, `city`, `state_id`) VALUES
(1, 'North and Middle Andaman', 32),
(2, 'South Andaman', 32),
(3, 'Nicobar', 32),
(4, 'Adilabad', 1),
(5, 'Anantapur', 1),
(6, 'Chittoor', 1),
(7, 'East Godavari', 1),
(8, 'Guntur', 1),
(9, 'Hyderabad', 1),
(10, 'Kadapa', 1),
(11, 'Karimnagar', 1),
(12, 'Khammam', 1),
(13, 'Krishna', 1),
(14, 'Kurnool', 1),
(15, 'Mahbubnagar', 1),
(16, 'Medak', 1),
(17, 'Nalgonda', 1),
(18, 'Nellore', 1),
(19, 'Nizamabad', 1),
(20, 'Prakasam', 1),
(21, 'Rangareddi', 1),
(22, 'Srikakulam', 1),
(23, 'Vishakhapatnam', 1),
(24, 'Vizianagaram', 1),
(25, 'Warangal', 1),
(26, 'West Godavari', 1),
(27, 'Anjaw', 3),
(28, 'Changlang', 3),
(29, 'East Kameng', 3),
(30, 'Lohit', 3),
(31, 'Lower Subansiri', 3),
(32, 'Papum Pare', 3),
(33, 'Tirap', 3),
(34, 'Dibang Valley', 3),
(35, 'Upper Subansiri', 3),
(36, 'West Kameng', 3),
(37, 'Barpeta', 2),
(38, 'Bongaigaon', 2),
(39, 'Cachar', 2),
(40, 'Darrang', 2),
(41, 'Dhemaji', 2),
(42, 'Dhubri', 2),
(43, 'Dibrugarh', 2),
(44, 'Goalpara', 2),
(45, 'Golaghat', 2),
(46, 'Hailakandi', 2),
(47, 'Jorhat', 2),
(48, 'Karbi Anglong', 2),
(49, 'Karimganj', 2),
(50, 'Kokrajhar', 2),
(51, 'Lakhimpur', 2),
(52, 'Marigaon', 2),
(53, 'Nagaon', 2),
(54, 'Nalbari', 2),
(55, 'North Cachar Hills', 2),
(56, 'Sibsagar', 2),
(57, 'Sonitpur', 2),
(58, 'Tinsukia', 2),
(59, 'Araria', 4),
(60, 'Aurangabad', 4),
(61, 'Banka', 4),
(62, 'Begusarai', 4),
(63, 'Bhagalpur', 4),
(64, 'Bhojpur', 4),
(65, 'Buxar', 4),
(66, 'Darbhanga', 4),
(67, 'Purba Champaran', 4),
(68, 'Gaya', 4),
(69, 'Gopalganj', 4),
(70, 'Jamui', 4),
(71, 'Jehanabad', 4),
(72, 'Khagaria', 4),
(73, 'Kishanganj', 4),
(74, 'Kaimur', 4),
(75, 'Katihar', 4),
(76, 'Lakhisarai', 4),
(77, 'Madhubani', 4),
(78, 'Munger', 4),
(79, 'Madhepura', 4),
(80, 'Muzaffarpur', 4),
(81, 'Nalanda', 4),
(82, 'Nawada', 4),
(83, 'Patna', 4),
(84, 'Purnia', 4),
(85, 'Rohtas', 4),
(86, 'Saharsa', 4),
(87, 'Samastipur', 4),
(88, 'Sheohar', 4),
(89, 'Sheikhpura', 4),
(90, 'Saran', 4),
(91, 'Sitamarhi', 4),
(92, 'Supaul', 4),
(93, 'Siwan', 4),
(94, 'Vaishali', 4),
(95, 'Pashchim Champaran', 4),
(96, 'Bastar', 36),
(97, 'Bilaspur', 36),
(98, 'Dantewada', 36),
(99, 'Dhamtari', 36),
(100, 'Durg', 36),
(101, 'Jashpur', 36),
(102, 'Janjgir-Champa', 36),
(103, 'Korba', 36),
(104, 'Koriya', 36),
(105, 'Kanker', 36),
(106, 'Kawardha', 36),
(107, 'Mahasamund', 36),
(108, 'Raigarh', 36),
(109, 'Rajnandgaon', 36),
(110, 'Raipur', 36),
(111, 'Surguja', 36),
(112, 'Diu', 29),
(113, 'Daman', 29),
(114, 'Central Delhi', 25),
(115, 'East Delhi', 25),
(116, 'New Delhi', 25),
(117, 'North Delhi', 25),
(118, 'North East Delhi', 25),
(119, 'North West Delhi', 25),
(120, 'South Delhi', 25),
(121, 'South West Delhi', 25),
(122, 'West Delhi', 25),
(123, 'North Goa', 26),
(124, 'South Goa', 26),
(125, 'Ahmedabad', 5),
(126, 'Amreli District', 5),
(127, 'Anand', 5),
(128, 'Banaskantha', 5),
(129, 'Bharuch', 5),
(130, 'Bhavnagar', 5),
(131, 'Dahod', 5),
(132, 'The Dangs', 5),
(133, 'Gandhinagar', 5),
(134, 'Jamnagar', 5),
(135, 'Junagadh', 5),
(136, 'Kutch', 5),
(137, 'Kheda', 5),
(138, 'Mehsana', 5),
(139, 'Narmada', 5),
(140, 'Navsari', 5),
(141, 'Patan', 5),
(142, 'Panchmahal', 5),
(143, 'Porbandar', 5),
(144, 'Rajkot', 5),
(145, 'Sabarkantha', 5),
(146, 'Surendranagar', 5),
(147, 'Surat', 5),
(148, 'Vadodara', 5),
(149, 'Valsad', 5),
(150, 'Ambala', 6),
(151, 'Bhiwani', 6),
(152, 'Faridabad', 6),
(153, 'Fatehabad', 6),
(154, 'Gurgaon', 6),
(155, 'Hissar', 6),
(156, 'Jhajjar', 6),
(157, 'Jind', 6),
(158, 'Karnal', 6),
(159, 'Kaithal', 6),
(160, 'Kurukshetra', 6),
(161, 'Mahendragarh', 6),
(162, 'Mewat', 6),
(163, 'Panchkula', 6),
(164, 'Panipat', 6),
(165, 'Rewari', 6),
(166, 'Rohtak', 6),
(167, 'Sirsa', 6),
(168, 'Sonepat', 6),
(169, 'Yamuna Nagar', 6),
(170, 'Palwal', 6),
(171, 'Bilaspur', 7),
(172, 'Chamba', 7),
(173, 'Hamirpur', 7),
(174, 'Kangra', 7),
(175, 'Kinnaur', 7),
(176, 'Kulu', 7),
(177, 'Lahaul and Spiti', 7),
(178, 'Mandi', 7),
(179, 'Shimla', 7),
(180, 'Sirmaur', 7),
(181, 'Solan', 7),
(182, 'Una', 7),
(183, 'Anantnag', 8),
(184, 'Badgam', 8),
(185, 'Bandipore', 8),
(186, 'Baramula', 8),
(187, 'Doda', 8),
(188, 'Jammu', 8),
(189, 'Kargil', 8),
(190, 'Kathua', 8),
(191, 'Kupwara', 8),
(192, 'Leh', 8),
(193, 'Poonch', 8),
(194, 'Pulwama', 8),
(195, 'Rajauri', 8),
(196, 'Srinagar', 8),
(197, 'Samba', 8),
(198, 'Udhampur', 8),
(199, 'Bokaro', 34),
(200, 'Chatra', 34),
(201, 'Deoghar', 34),
(202, 'Dhanbad', 34),
(203, 'Dumka', 34),
(204, 'Purba Singhbhum', 34),
(205, 'Garhwa', 34),
(206, 'Giridih', 34),
(207, 'Godda', 34),
(208, 'Gumla', 34),
(209, 'Hazaribagh', 34),
(210, 'Koderma', 34),
(211, 'Lohardaga', 34),
(212, 'Pakur', 34),
(213, 'Palamu', 34),
(214, 'Ranchi', 34),
(215, 'Sahibganj', 34),
(216, 'Seraikela and Kharsawan', 34),
(217, 'Pashchim Singhbhum', 34),
(218, 'Ramgarh', 34),
(219, 'Bidar', 9),
(220, 'Belgaum', 9),
(221, 'Bijapur', 9),
(222, 'Bagalkot', 9),
(223, 'Bellary', 9),
(224, 'Bangalore Rural District', 9),
(225, 'Bangalore Urban District', 9),
(226, 'Chamarajnagar', 9),
(227, 'Chikmagalur', 9),
(228, 'Chitradurga', 9),
(229, 'Davanagere', 9),
(230, 'Dharwad', 9),
(231, 'Dakshina Kannada', 9),
(232, 'Gadag', 9),
(233, 'Gulbarga', 9),
(234, 'Hassan', 9),
(235, 'Haveri District', 9),
(236, 'Kodagu', 9),
(237, 'Kolar', 9),
(238, 'Koppal', 9),
(239, 'Mandya', 9),
(240, 'Mysore', 9),
(241, 'Raichur', 9),
(242, 'Shimoga', 9),
(243, 'Tumkur', 9),
(244, 'Udupi', 9),
(245, 'Uttara Kannada', 9),
(246, 'Ramanagara', 9),
(247, 'Chikballapur', 9),
(248, 'Yadagiri', 9),
(249, 'Alappuzha', 10),
(250, 'Ernakulam', 10),
(251, 'Idukki', 10),
(252, 'Kollam', 10),
(253, 'Kannur', 10),
(254, 'Kasaragod', 10),
(255, 'Kottayam', 10),
(256, 'Kozhikode', 10),
(257, 'Malappuram', 10),
(258, 'Palakkad', 10),
(259, 'Pathanamthitta', 10),
(260, 'Thrissur', 10),
(261, 'Thiruvananthapuram', 10),
(262, 'Wayanad', 10),
(263, 'Alirajpur', 11),
(264, 'Anuppur', 11),
(265, 'Ashok Nagar', 11),
(266, 'Balaghat', 11),
(267, 'Barwani', 11),
(268, 'Betul', 11),
(269, 'Bhind', 11),
(270, 'Bhopal', 11),
(271, 'Burhanpur', 11),
(272, 'Chhatarpur', 11),
(273, 'Chhindwara', 11),
(274, 'Damoh', 11),
(275, 'Datia', 11),
(276, 'Dewas', 11),
(277, 'Dhar', 11),
(278, 'Dindori', 11),
(279, 'Guna', 11),
(280, 'Gwalior', 11),
(281, 'Harda', 11),
(282, 'Hoshangabad', 11),
(283, 'Indore', 11),
(284, 'Jabalpur', 11),
(285, 'Jhabua', 11),
(286, 'Katni', 11),
(287, 'Khandwa', 11),
(288, 'Khargone', 11),
(289, 'Mandla', 11),
(290, 'Mandsaur', 11),
(291, 'Morena', 11),
(292, 'Narsinghpur', 11),
(293, 'Neemuch', 11),
(294, 'Panna', 11),
(295, 'Rewa', 11),
(296, 'Rajgarh', 11),
(297, 'Ratlam', 11),
(298, 'Raisen', 11),
(299, 'Sagar', 11),
(300, 'Satna', 11),
(301, 'Sehore', 11),
(302, 'Seoni', 11),
(303, 'Shahdol', 11),
(304, 'Shajapur', 11),
(305, 'Sheopur', 11),
(306, 'Shivpuri', 11),
(307, 'Sidhi', 11),
(308, 'Singrauli', 11),
(309, 'Tikamgarh', 11),
(310, 'Ujjain', 11),
(311, 'Umaria', 11),
(312, 'Vidisha', 11),
(313, 'Ahmednagar', 12),
(314, 'Akola', 12),
(315, 'Amrawati', 12),
(316, 'Aurangabad', 12),
(317, 'Bhandara', 12),
(318, 'Beed', 12),
(319, 'Buldhana', 12),
(320, 'Chandrapur', 12),
(321, 'Dhule', 12),
(322, 'Gadchiroli', 12),
(323, 'Gondiya', 12),
(324, 'Hingoli', 12),
(325, 'Jalgaon', 12),
(326, 'Jalna', 12),
(327, 'Kolhapur', 12),
(328, 'Latur', 12),
(329, 'Mumbai City', 12),
(330, 'Mumbai suburban', 12),
(331, 'Nandurbar', 12),
(332, 'Nanded', 12),
(333, 'Nagpur', 12),
(334, 'Nashik', 12),
(335, 'Osmanabad', 12),
(336, 'Parbhani', 12),
(337, 'Pune', 12),
(338, 'Raigad', 12),
(339, 'Ratnagiri', 12),
(340, 'Sindhudurg', 12),
(341, 'Sangli', 12),
(342, 'Solapur', 12),
(343, 'Satara', 12),
(344, 'Thane', 12),
(345, 'Wardha', 12),
(346, 'Washim', 12),
(347, 'Yavatmal', 12),
(348, 'Bishnupur', 13),
(349, 'Churachandpur', 13),
(350, 'Chandel', 13),
(351, 'Imphal East', 13),
(352, 'Senapati', 13),
(353, 'Tamenglong', 13),
(354, 'Thoubal', 13),
(355, 'Ukhrul', 13),
(356, 'Imphal West', 13),
(357, 'East Garo Hills', 14),
(358, 'East Khasi Hills', 14),
(359, 'Jaintia Hills', 14),
(360, 'Ri-Bhoi', 14),
(361, 'South Garo Hills', 14),
(362, 'West Garo Hills', 14),
(363, 'West Khasi Hills', 14),
(364, 'Aizawl', 15),
(365, 'Champhai', 15),
(366, 'Kolasib', 15),
(367, 'Lawngtlai', 15),
(368, 'Lunglei', 15),
(369, 'Mamit', 15),
(370, 'Saiha', 15),
(371, 'Serchhip', 15),
(372, 'Dimapur', 16),
(373, 'Kohima', 16),
(374, 'Mokokchung', 16),
(375, 'Mon', 16),
(376, 'Phek', 16),
(377, 'Tuensang', 16),
(378, 'Wokha', 16),
(379, 'Zunheboto', 16),
(380, 'Angul', 17),
(381, 'Boudh', 17),
(382, 'Bhadrak', 17),
(383, 'Bolangir', 17),
(384, 'Bargarh', 17),
(385, 'Baleswar', 17),
(386, 'Cuttack', 17),
(387, 'Debagarh', 17),
(388, 'Dhenkanal', 17),
(389, 'Ganjam', 17),
(390, 'Gajapati', 17),
(391, 'Jharsuguda', 17),
(392, 'Jajapur', 17),
(393, 'Jagatsinghpur', 17),
(394, 'Khordha', 17),
(395, 'Kendujhar', 17),
(396, 'Kalahandi', 17),
(397, 'Kandhamal', 17),
(398, 'Koraput', 17),
(399, 'Kendrapara', 17),
(400, 'Malkangiri', 17),
(401, 'Mayurbhanj', 17),
(402, 'Nabarangpur', 17),
(403, 'Nuapada', 17),
(404, 'Nayagarh', 17),
(405, 'Puri', 17),
(406, 'Rayagada', 17),
(407, 'Sambalpur', 17),
(408, 'Subarnapur', 17),
(409, 'Sundargarh', 17),
(410, 'Karaikal', 27),
(411, 'Mahe', 27),
(412, 'Puducherry', 27),
(413, 'Yanam', 27),
(414, 'Amritsar', 18),
(415, 'Bathinda', 18),
(416, 'Firozpur', 18),
(417, 'Faridkot', 18),
(418, 'Fatehgarh Sahib', 18),
(419, 'Gurdaspur', 18),
(420, 'Hoshiarpur', 18),
(421, 'Jalandhar', 18),
(422, 'Kapurthala', 18),
(423, 'Ludhiana', 18),
(424, 'Mansa', 18),
(425, 'Moga', 18),
(426, 'Mukatsar', 18),
(427, 'Nawan Shehar', 18),
(428, 'Patiala', 18),
(429, 'Rupnagar', 18),
(430, 'Sangrur', 18),
(431, 'Ajmer', 19),
(432, 'Alwar', 19),
(433, 'Bikaner', 19),
(434, 'Barmer', 19),
(435, 'Banswara', 19),
(436, 'Bharatpur', 19),
(437, 'Baran', 19),
(438, 'Bundi', 19),
(439, 'Bhilwara', 19),
(440, 'Churu', 19),
(441, 'Chittorgarh', 19),
(442, 'Dausa', 19),
(443, 'Dholpur', 19),
(444, 'Dungapur', 19),
(445, 'Ganganagar', 19),
(446, 'Hanumangarh', 19),
(447, 'Juhnjhunun', 19),
(448, 'Jalore', 19),
(449, 'Jodhpur', 19),
(450, 'Jaipur', 19),
(451, 'Jaisalmer', 19),
(452, 'Jhalawar', 19),
(453, 'Karauli', 19),
(454, 'Kota', 19),
(455, 'Nagaur', 19),
(456, 'Pali', 19),
(457, 'Pratapgarh', 19),
(458, 'Rajsamand', 19),
(459, 'Sikar', 19),
(460, 'Sawai Madhopur', 19),
(461, 'Sirohi', 19),
(462, 'Tonk', 19),
(463, 'Udaipur', 19),
(464, 'East Sikkim', 20),
(465, 'North Sikkim', 20),
(466, 'South Sikkim', 20),
(467, 'West Sikkim', 20),
(468, 'Ariyalur', 21),
(469, 'Chennai', 21),
(470, 'Coimbatore', 21),
(471, 'Cuddalore', 21),
(472, 'Dharmapuri', 21),
(473, 'Dindigul', 21),
(474, 'Erode', 21),
(475, 'Kanchipuram', 21),
(476, 'Kanyakumari', 21),
(477, 'Karur', 21),
(478, 'Madurai', 21),
(479, 'Nagapattinam', 21),
(480, 'The Nilgiris', 21),
(481, 'Namakkal', 21),
(482, 'Perambalur', 21),
(483, 'Pudukkottai', 21),
(484, 'Ramanathapuram', 21),
(485, 'Salem', 21),
(486, 'Sivagangai', 21),
(487, 'Tiruppur', 21),
(488, 'Tiruchirappalli', 21),
(489, 'Theni', 21),
(490, 'Tirunelveli', 21),
(491, 'Thanjavur', 21),
(492, 'Thoothukudi', 21),
(493, 'Thiruvallur', 21),
(494, 'Thiruvarur', 21),
(495, 'Tiruvannamalai', 21),
(496, 'Vellore', 21),
(497, 'Villupuram', 21),
(498, 'Dhalai', 22),
(499, 'North Tripura', 22),
(500, 'South Tripura', 22),
(501, 'West Tripura', 22),
(502, 'Almora', 33),
(503, 'Bageshwar', 33),
(504, 'Chamoli', 33),
(505, 'Champawat', 33),
(506, 'Dehradun', 33),
(507, 'Haridwar', 33),
(508, 'Nainital', 33),
(509, 'Pauri Garhwal', 33),
(510, 'Pithoragharh', 33),
(511, 'Rudraprayag', 33),
(512, 'Tehri Garhwal', 33),
(513, 'Udham Singh Nagar', 33),
(514, 'Uttarkashi', 33),
(515, 'Agra', 23),
(516, 'Allahabad', 23),
(517, 'Aligarh', 23),
(518, 'Ambedkar Nagar', 23),
(519, 'Auraiya', 23),
(520, 'Azamgarh', 23),
(521, 'Barabanki', 23),
(522, 'Badaun', 23),
(523, 'Bagpat', 23),
(524, 'Bahraich', 23),
(525, 'Bijnor', 23),
(526, 'Ballia', 23),
(527, 'Banda', 23),
(528, 'Balrampur', 23),
(529, 'Bareilly', 23),
(530, 'Basti', 23),
(531, 'Bulandshahr', 23),
(532, 'Chandauli', 23),
(533, 'Chitrakoot', 23),
(534, 'Deoria', 23),
(535, 'Etah', 23),
(536, 'Kanshiram Nagar', 23),
(537, 'Etawah', 23),
(538, 'Firozabad', 23),
(539, 'Farrukhabad', 23),
(540, 'Fatehpur', 23),
(541, 'Faizabad', 23),
(542, 'Gautam Buddha Nagar', 23),
(543, 'Gonda', 23),
(544, 'Ghazipur', 23),
(545, 'Gorkakhpur', 23),
(546, 'Ghaziabad', 23),
(547, 'Hamirpur', 23),
(548, 'Hardoi', 23),
(549, 'Mahamaya Nagar', 23),
(550, 'Jhansi', 23),
(551, 'Jalaun', 23),
(552, 'Jyotiba Phule Nagar', 23),
(553, 'Jaunpur District', 23),
(554, 'Kanpur Dehat', 23),
(555, 'Kannauj', 23),
(556, 'Kanpur Nagar', 23),
(557, 'Kaushambi', 23),
(558, 'Kushinagar', 23),
(559, 'Lalitpur', 23),
(560, 'Lakhimpur Kheri', 23),
(561, 'Lucknow', 23),
(562, 'Mau', 23),
(563, 'Meerut', 23),
(564, 'Maharajganj', 23),
(565, 'Mahoba', 23),
(566, 'Mirzapur', 23),
(567, 'Moradabad', 23),
(568, 'Mainpuri', 23),
(569, 'Mathura', 23),
(570, 'Muzaffarnagar', 23),
(571, 'Pilibhit', 23),
(572, 'Pratapgarh', 23),
(573, 'Rampur', 23),
(574, 'Rae Bareli', 23),
(575, 'Saharanpur', 23),
(576, 'Sitapur', 23),
(577, 'Shahjahanpur', 23),
(578, 'Sant Kabir Nagar', 23),
(579, 'Siddharthnagar', 23),
(580, 'Sonbhadra', 23),
(581, 'Sant Ravidas Nagar', 23),
(582, 'Sultanpur', 23),
(583, 'Shravasti', 23),
(584, 'Unnao', 23),
(585, 'Varanasi', 23),
(586, 'Birbhum', 24),
(587, 'Bankura', 24),
(588, 'Bardhaman', 24),
(589, 'Darjeeling', 24),
(590, 'Dakshin Dinajpur', 24),
(591, 'Hooghly', 24),
(592, 'Howrah', 24),
(593, 'Jalpaiguri', 24),
(594, 'Cooch Behar', 24),
(595, 'Kolkata', 24),
(596, 'Malda', 24),
(597, 'Midnapore', 24),
(598, 'Murshidabad', 24),
(599, 'Nadia', 24),
(600, 'North 24 Parganas', 24),
(601, 'South 24 Parganas', 24),
(602, 'Purulia', 24),
(603, 'Uttar Dinajpur', 24);

-- --------------------------------------------------------

--
-- Table structure for table `contact_tbl`
--

CREATE TABLE `contact_tbl` (
  `contact_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `subject` longtext NOT NULL,
  `comments` longtext NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact_tbl`
--

INSERT INTO `contact_tbl` (`contact_id`, `name`, `email`, `subject`, `comments`, `created_at`) VALUES
(1, 'asdasd', 'saviobabu007@gmail.com', 'the hrjhdjhfjdhfjfjdf', 'thdsjhfdsjfj sdf jdhsfjdskjhfkj sdkjfkjds', '2023-05-14 18:40:03');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-05-06 07:54:17.820020'),
(2, 'auth', '0001_initial', '2023-05-06 07:54:18.752907'),
(3, 'admin', '0001_initial', '2023-05-06 07:54:19.002428'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-05-06 07:54:19.058450'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-06 07:54:19.074450'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-05-06 07:54:19.179448'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-05-06 07:54:19.269102'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-05-06 07:54:19.309114'),
(9, 'auth', '0004_alter_user_username_opts', '2023-05-06 07:54:19.325123'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-05-06 07:54:19.397136'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-05-06 07:54:19.409147'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-05-06 07:54:19.421785'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-05-06 07:54:19.462965'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-05-06 07:54:19.503868'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-05-06 07:54:19.535467'),
(16, 'auth', '0011_update_proxy_permissions', '2023-05-06 07:54:19.559448'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-05-06 07:54:19.607462'),
(18, 'sessions', '0001_initial', '2023-05-06 07:54:19.671476');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2hg22zoi4w1f1kgyflomnj3qiaeyddad', '.eJyFkU1LxDAQhv_KknORtrbduCcRLwuyB4-KhDFJu6FpUpPpYV363510t6ggWAh03nnzZD7OzERhfddpxXYYJp0xBQhsd2ZT1EEYkos8Yw4GzXYMdUSWMT2AsRSCGoy771J0I_1AmfHoXTLm27wo86os6oZUafCUSE1GV1TQMZIl9m1UdDbK0o_tbVRtT2Y8jUTIZ4LBadAOUzFrUYnCfFBU2tNHXeNL7kv_yTmkqhzSO2ueBBj8lK5v8-VbBTFCwnzHatI_THIKQTuZQPvDM2GCltqMxGElp9C37XUwbrI2YxEBp9SQDBqQ5khcRD2MGJdHnKepsd3rW7Y6BBCsaHhV8IpXNXVqIaIwjiaOS4fLQ-_GWuM6sfYewer4YHq9fyTL3dUhfq9mkf7ewiVlnPQqJRt-WxfFqv-_FwB1hHDwiVsW1aaueLlp6rulVO97cVkcS0iQaLxLQcnmef4CQD7Bcg:1pyfPi:N8E0LJXibyvHFOAuSXyBymEq9WCNILGY-vOYPKFUv-c', '2023-05-29 21:07:26.162527'),
('d4nbrc0nbsjj2gnbp8tr7h28wmwgteng', '.eJwVij0KwCAMRu_yzVJoR6feREINIjRaNA5FvHvT8f1M5B7umhJHeG2DHSIpwU-Mzi1k07tDIWF4KHeFAwvl25Ci5HKmn7arihV9H_uOtT4p4h1d:1q16WA:tcyARlVjfRakUUcnhXELi-jwv2HNAUA-EBb4ZCJZYOU', '2023-06-05 14:28:10.269690'),
('m9qslazwe6nthev2lv5lxzi7i1agk31r', '.eJwVi0sKwzAMRK9StDbFDv2AV71JEJXiGv-C5SxCyN2rLAZm3swcEGXOLQQm8KNvbIBwIPgDNuE-R8XOGqhYGDwMlgEGuGDMGpFKrJ9wpfu3FW3WX6vX0L6tm-xjcs-XUiTqLKJc0iKkulFWk1MWWpIuxr7qzZ7nH3GfLwo:1pvvVp:ZdDOCD7_j3KMAlh2U8hElUTUYI1cQIeQj2IEd4BCCGs', '2023-05-22 07:42:25.263599'),
('mq4in8k2kgqxa6vs6lehfe132yi6c0s4', '.eJwdjbtuwkAQRX8lmtpGXguw5CqGNAjRpYHGWjLj9cb70s66iBD_zpBipHvPPdI8wPLoojGE0Je8UgWoi4b-AStTHq1gVUHQnqCHQlygAvLaOqkavQ2f5t02P9HLkuYY3mLTNapttq3a7YVqxEzMwnmZGOU-0Elwi2OcFjHKX6L_R4aLDSK23TAMx-NWdbsvdbuKYnFMOcZJRtTBkquXmJO29Xz_Pp_u68UfTvUaODnN8-Y3GXg-Xx0MR_4:1pvTak:QQCEPiW7opReW_kDfXrCoKtPkPyglTqQnqdzGYsTFEk', '2023-05-21 01:53:38.868557');

-- --------------------------------------------------------

--
-- Table structure for table `reset_pass_tbl`
--

CREATE TABLE `reset_pass_tbl` (
  `reset_id` int(11) NOT NULL,
  `email` varchar(250) NOT NULL,
  `user_id` int(11) NOT NULL,
  `code` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reset_pass_tbl`
--

INSERT INTO `reset_pass_tbl` (`reset_id`, `email`, `user_id`, `code`, `created_at`, `status`) VALUES
(6, 'sav@gmail.com', 11, 'khzbu', '2023-05-16 17:50:55', 0),
(7, '42', 1, 'ufcld', '2023-05-16 18:13:03', 1),
(8, '42', 1, 'bfzpk', '2023-05-16 18:13:50', 1),
(9, 'admin@gmail.com', 1, 'ielbw', '2023-05-16 18:16:46', 1),
(10, 'admin@gmail.com', 1, 'kzlct', '2023-05-16 18:17:34', 1),
(11, 'admin@gmail.com', 1, 'boslf', '2023-05-16 18:26:24', 0),
(12, 'admin1@gmail.com', 2, 'sstlv', '2023-05-16 18:28:24', 1),
(13, 'admin1@gmail.com', 2, 'utyyu', '2023-05-16 18:31:31', 0),
(14, 'admin@gmail.com', 1, 'rfbdt', '2023-05-16 18:48:49', 1),
(15, 'admin@gmail.com', 1, 'kvzzz', '2023-05-16 18:49:46', 1),
(16, 'admin@gmail.com', 1, 'yviuy', '2023-05-16 18:55:24', 0),
(17, 'admin@gmail.com', 1, 'ynnhr', '2023-05-16 18:57:30', 0),
(18, 'admin@gmail.com', 1, 'vaexi', '2023-05-16 18:58:53', 0),
(19, 'admin@gmail.com', 1, 'vaohm', '2023-05-21 16:11:03', 1),
(20, 'admin@gmail.com', 1, 'cnepy', '2023-05-21 16:12:50', 1),
(21, 'admin@gmail.com', 1, 'jxiye', '2023-05-21 16:12:54', 1),
(22, 'admin@gmail.com', 1, 'igaso', '2023-05-21 16:16:54', 0),
(23, 'admin2@gmail.com', 12, 'zblpv', '2023-05-22 12:22:13', 1),
(24, 'admin2@gmail.com', 13, 'tvial', '2023-05-22 12:25:34', 1),
(25, 'admin2@gmail.com', 14, 'blmcm', '2023-05-22 12:26:47', 1),
(26, 'admin2@gmail.com', 15, 'rxrpl', '2023-05-22 12:27:18', 1),
(27, 'admin2@gmail.com', 16, 'cdmba', '2023-05-22 12:45:01', 1),
(28, 'admin2@gmail.com', 17, 'serie', '2023-05-22 13:23:38', 1),
(29, 'admin2@gmail.com', 20, 'ayhjp', '2023-05-22 13:38:37', 1),
(30, 'Admin2@gmail.com', 21, 'maaaq', '2023-05-22 13:43:33', 0),
(31, 'admin3@gmail.com', 22, 'zqdnw', '2023-05-22 14:01:41', 0);

-- --------------------------------------------------------

--
-- Table structure for table `sales_bike_img_tbl`
--

CREATE TABLE `sales_bike_img_tbl` (
  `image_id` int(11) NOT NULL,
  `image_name` varchar(250) NOT NULL,
  `sales_bike_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sales_bike_img_tbl`
--

INSERT INTO `sales_bike_img_tbl` (`image_id`, `image_name`, `sales_bike_id`, `created_at`, `status`) VALUES
(13, '2019-Aprilia-Shiver-900.jpg', 10, '2023-05-10 09:31:30', 1),
(14, '65770.png', 10, '2023-05-10 09:31:30', 1),
(15, '80621.jpg', 10, '2023-05-10 09:31:30', 1),
(16, '20210902155351.jpg', 10, '2023-05-10 09:31:54', 1);

-- --------------------------------------------------------

--
-- Table structure for table `sales_bike_tbl`
--

CREATE TABLE `sales_bike_tbl` (
  `bike_id` int(11) NOT NULL,
  `bike_name` varchar(150) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `ser_center_id` int(11) NOT NULL,
  `min_advance` float NOT NULL,
  `price` float NOT NULL,
  `stock` bigint(20) NOT NULL,
  `descr` mediumtext NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sales_bike_tbl`
--

INSERT INTO `sales_bike_tbl` (`bike_id`, `bike_name`, `brand_id`, `ser_center_id`, `min_advance`, `price`, `stock`, `descr`, `created_at`, `status`) VALUES
(10, 'panega 1200', 8, 1, 200, 60000, 11, 'skfjdkslfjdklsfjsdkjf jsdklfjl', '2023-05-16 05:57:36', 1);

-- --------------------------------------------------------

--
-- Table structure for table `service_book_img_tbl`
--

CREATE TABLE `service_book_img_tbl` (
  `service_book_img_id` int(11) NOT NULL,
  `service_book_id` int(11) NOT NULL,
  `image` varchar(250) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_book_img_tbl`
--

INSERT INTO `service_book_img_tbl` (`service_book_img_id`, `service_book_id`, `image`, `created_at`) VALUES
(4, 11, '2019-Aprilia-Shiver-900.jpg', '2023-05-15 12:50:31'),
(5, 11, '65770.png', '2023-05-15 12:50:31'),
(6, 11, '80621.jpg', '2023-05-15 12:50:31'),
(7, 11, '80621.jpg', '2023-05-15 12:50:31'),
(8, 11, 'MY-22-Panigale-V4-S-Model-Blocks-630x390-V06.png', '2023-05-15 12:50:31'),
(9, 11, 'Model-Menu-MY20-Panigale-V2-White.png', '2023-05-15 12:50:31'),
(10, 11, 'MY-22-Panigale-V4-S-Model-Blocks-630x390-V06.png', '2023-05-15 12:50:31'),
(11, 11, 'side-view-6.png', '2023-05-15 12:50:31');

-- --------------------------------------------------------

--
-- Table structure for table `service_book_tbl`
--

CREATE TABLE `service_book_tbl` (
  `service_book_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `complaints` longtext NOT NULL,
  `worker_note` longtext DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `lng` double DEFAULT NULL,
  `bike_brand_id` int(11) NOT NULL,
  `bike_model` varchar(100) NOT NULL,
  `number_plate` varchar(150) NOT NULL,
  `alternate_phone` varchar(50) NOT NULL,
  `bill_amount` double DEFAULT NULL,
  `pickup_mode` tinyint(1) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `estimate_delivery` timestamp NOT NULL DEFAULT current_timestamp(),
  `bill_status` tinyint(1) NOT NULL,
  `status` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_book_tbl`
--

INSERT INTO `service_book_tbl` (`service_book_id`, `service_id`, `user_id`, `complaints`, `worker_note`, `lat`, `lng`, `bike_brand_id`, `bike_model`, `number_plate`, `alternate_phone`, `bill_amount`, `pickup_mode`, `created_at`, `estimate_delivery`, `bill_status`, `status`) VALUES
(7, 4, 11, 'sfsfdsfsfs dfdsf sfsfs fsfsfs', '', 10.0171776, 76.2707968, 4, 'ffsfsdfsf', 'KL 21 K 6200', '7012545907', 2500, 1, '2023-05-11 08:07:07', '2023-05-16 08:07:07', 1, 4),
(8, 4, 11, 'sfsdfdsfdsfsdfsfsdf', 'sdfjsd fjsdjf djsfsd fdshfkj hsdkjhfkjsdhfjhsdj hfjsfjsdj fsdjf jhdskjfhkjsdhf kjsdkjfhdjsfjhsdkjfkjdhskjfhkj', 0, 0, 4, 'ffsfsdfsf', 'KL 41 K 6200', '7012545907', 2500, 0, '2023-05-11 08:18:40', '2023-05-16 08:18:40', 0, 6),
(9, 5, 11, 'oil change with checkup', '', 10.0040704, 76.2740736, 7, '390', 'KL 42 M 2500', '7012548031', 5400, 1, '2023-05-11 14:36:48', '2023-05-16 14:36:48', 0, 1),
(10, 6, 11, 'oild skjdfkdjfkjksdfjkdjs f', '', 10.0040704, 76.2740736, 6, 'CT 100', 'KL 41 M 6200', '7012545908', 2500, 1, '2023-05-11 19:57:49', '2023-05-16 19:57:49', 0, 0),
(11, 4, 10, 'sdfkjsdkfjdsfkldsfkljdskfjdklsfjkldsjfkldjsklfjdklsjfkldjsf', '', 0, 0, 4, 'ssdfsdf', 'KL 41 N 6200', '7012545907', 2500, 0, '2023-05-15 07:49:20', '2023-05-20 07:49:20', 0, 4),
(12, 4, 10, 'sdfkjsdkfjdsfkldsfkljdskfjdklsfjkldsjfkldjsklfjdklsjfkldjsf', '', 0, 0, 4, 'ssdfsdf', 'KL 41 Z 6200', '7012545907', 2500, 0, '2023-05-15 07:49:28', '2023-05-20 07:49:28', 0, 5),
(13, 4, 10, 'sdfkjsdkfjdsfkldsfkljdskfjdklsfjkldsjfkldjsklfjdklsjfkldjsf', '', 0, 0, 4, 'ssdfsdf', 'KL 41 Z 6205', '7012545906', 2500, 0, '2023-05-15 07:49:41', '2023-05-20 07:49:41', 0, 4);

-- --------------------------------------------------------

--
-- Table structure for table `service_center_table`
--

CREATE TABLE `service_center_table` (
  `service_center_id` int(11) NOT NULL,
  `center_name` varchar(100) NOT NULL,
  `city_id` int(11) NOT NULL,
  `address` varchar(250) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `passw` varchar(250) NOT NULL,
  `id_proof` varchar(250) NOT NULL,
  `gstin` varchar(250) NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `type` tinyint(1) NOT NULL,
  `status` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_center_table`
--

INSERT INTO `service_center_table` (`service_center_id`, `center_name`, `city_id`, `address`, `phone`, `email`, `passw`, `id_proof`, `gstin`, `create_date`, `type`, `status`) VALUES
(1, 'DreamLand', 42, 'skfsdkfs dlfsdlklsdfk', '07012042156', 'admin@gmail.com', '3c83751e645721983ba82566ba888881', '65770.png', '27AAACC4175D1ZY', '2023-05-21 17:45:50', 1, 2),
(3, 'testest', 382, 'this sfsjdf jsdf sdhfdkjs fhdskj hfdhsfh dks', '7012545907', 'admin1@gmail.com', '3c83751e645721983ba82566ba888881', '4-1020x350.jpg', '09AAACH7409R1ZZ', '2023-05-21 18:15:21', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `service_feedback_tbl`
--

CREATE TABLE `service_feedback_tbl` (
  `feedback_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `service_book_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_feedback_tbl`
--

INSERT INTO `service_feedback_tbl` (`feedback_id`, `user_id`, `service_book_id`, `rating`, `comment`, `created_at`) VALUES
(2, 10, 11, 5, 'best and cost less service. loved it', '2023-05-15 13:43:41'),
(3, 10, 13, 1, 'very bad service and executives are not customer firendly. ', '2023-05-15 13:45:37');

-- --------------------------------------------------------

--
-- Table structure for table `service_list_tbl`
--

CREATE TABLE `service_list_tbl` (
  `service_id` int(11) NOT NULL,
  `ser_center_id` int(11) NOT NULL,
  `image_name` varchar(250) NOT NULL,
  `service_name` varchar(150) NOT NULL,
  `expected_cost` float DEFAULT NULL,
  `descr` longtext NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_list_tbl`
--

INSERT INTO `service_list_tbl` (`service_id`, `ser_center_id`, `image_name`, `service_name`, `expected_cost`, `descr`, `date`, `status`) VALUES
(4, 1, '110-1109055_png-bike-background-hd-for-picsart-baik-bag.jpg', 'MANSOON SERVICE', 2500, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam hendrerit nisi sed sollicitudin pellentesque. Nunc posuere purus rhoncus pulvinar aliquam. Ut aliquet tristique nisl vitae volutpat. Nulla aliquet porttitor venenatis. Donec a dui et dui fringilla consectetur id nec massa. Aliquam erat volutpat. Sed ut dui ut lacus dictum fermentum vel tincidunt neque. Sed sed lacinia lectus. Duis sit amet sodales felis. Duis nunc eros, mattis at dui ac, convallis semper risus. In adipiscing ultrices tellus, in suscipit massa vehicula eu.', '2023-05-10 09:00:50', 1),
(5, 1, 'images-download-bike-png-hd-download-11562994198gyywyithwv.png', 'Summer checkup', 5400, 'bet sjfdkls fkldsklf sjdfkljs dkfklsdj fjdklsfkj sdklfkds fklskfjdksjkfjdklsjkjfkljdskjfkldjsklfjkl jdsklfjdsklfjkls djklfjsdklj fkldjsfk jsdklfjklsdj', '2023-05-10 09:35:46', 1);

-- --------------------------------------------------------

--
-- Table structure for table `states`
--

CREATE TABLE `states` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `country_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `states`
--

INSERT INTO `states` (`id`, `name`, `country_id`) VALUES
(1, 'ANDHRA PRADESH', 105),
(2, 'ASSAM', 105),
(3, 'ARUNACHAL PRADESH', 105),
(4, 'BIHAR', 105),
(5, 'GUJRAT', 105),
(6, 'HARYANA', 105),
(7, 'HIMACHAL PRADESH', 105),
(8, 'JAMMU & KASHMIR', 105),
(9, 'KARNATAKA', 105),
(10, 'KERALA', 105),
(11, 'MADHYA PRADESH', 105),
(12, 'MAHARASHTRA', 105),
(13, 'MANIPUR', 105),
(14, 'MEGHALAYA', 105),
(15, 'MIZORAM', 105),
(16, 'NAGALAND', 105),
(17, 'ORISSA', 105),
(18, 'PUNJAB', 105),
(19, 'RAJASTHAN', 105),
(20, 'SIKKIM', 105),
(21, 'TAMIL NADU', 105),
(22, 'TRIPURA', 105),
(23, 'UTTAR PRADESH', 105),
(24, 'WEST BENGAL', 105),
(25, 'DELHI', 105),
(26, 'GOA', 105),
(27, 'PONDICHERY', 105),
(28, 'LAKSHDWEEP', 105),
(29, 'DAMAN & DIU', 105),
(30, 'DADRA & NAGAR', 105),
(31, 'CHANDIGARH', 105),
(32, 'ANDAMAN & NICOBAR', 105),
(33, 'UTTARANCHAL', 105),
(34, 'JHARKHAND', 105),
(35, 'CHATTISGARH', 105);

-- --------------------------------------------------------

--
-- Table structure for table `user_addr_tbl`
--

CREATE TABLE `user_addr_tbl` (
  `address_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  `address` varchar(250) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_tbl`
--

CREATE TABLE `user_tbl` (
  `user_id` int(11) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `city_id` int(11) NOT NULL,
  `address` varchar(150) NOT NULL,
  `passw` varchar(150) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `type` tinyint(4) NOT NULL,
  `status` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_tbl`
--

INSERT INTO `user_tbl` (`user_id`, `fullname`, `email`, `phone`, `city_id`, `address`, `passw`, `date`, `type`, `status`) VALUES
(10, 'test', 'admin@gmail.com', '07012042156', 6, 'skfsdkfs dlfsdlklsdfk', '3c83751e645721983ba82566ba888881', '2023-05-06 04:57:25', 0, 1),
(11, 'TESRSET', 'sav@gmail.com', '7012545907', 252, 'keralas dajsdkjaksjdkljasdasd', '3c83751e645721983ba82566ba888881', '2023-05-10 17:03:52', 0, 0),
(22, 'savio babu', 'admin3@gmail.com', '7012545908', 28, 'sdkjhfsdf sdfkjhdskjfkjdsfk', '3c83751e645721983ba82566ba888881', '2023-05-22 19:31:23', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_tbl`
--
ALTER TABLE `admin_tbl`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bike_brand_tbl`
--
ALTER TABLE `bike_brand_tbl`
  ADD PRIMARY KEY (`brand_id`);

--
-- Indexes for table `bike_purchase_tbl`
--
ALTER TABLE `bike_purchase_tbl`
  ADD PRIMARY KEY (`purchase_id`),
  ADD KEY `purchase_sales_bike_id_fk` (`bike_id`),
  ADD KEY `purchase_user_id_fk` (`user_id`);

--
-- Indexes for table `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `state_id` (`state_id`);

--
-- Indexes for table `contact_tbl`
--
ALTER TABLE `contact_tbl`
  ADD PRIMARY KEY (`contact_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `reset_pass_tbl`
--
ALTER TABLE `reset_pass_tbl`
  ADD PRIMARY KEY (`reset_id`);

--
-- Indexes for table `sales_bike_img_tbl`
--
ALTER TABLE `sales_bike_img_tbl`
  ADD PRIMARY KEY (`image_id`),
  ADD KEY `saled_bike_id_fk` (`sales_bike_id`);

--
-- Indexes for table `sales_bike_tbl`
--
ALTER TABLE `sales_bike_tbl`
  ADD PRIMARY KEY (`bike_id`),
  ADD KEY `sales_bike_ser_center_id_fk` (`ser_center_id`),
  ADD KEY `sales_bike_brand_id_fk` (`brand_id`);

--
-- Indexes for table `service_book_img_tbl`
--
ALTER TABLE `service_book_img_tbl`
  ADD PRIMARY KEY (`service_book_img_id`);

--
-- Indexes for table `service_book_tbl`
--
ALTER TABLE `service_book_tbl`
  ADD PRIMARY KEY (`service_book_id`),
  ADD KEY `service_book_user_id_fk` (`user_id`),
  ADD KEY `service_book_bike_brand_fk` (`bike_brand_id`);

--
-- Indexes for table `service_center_table`
--
ALTER TABLE `service_center_table`
  ADD PRIMARY KEY (`service_center_id`),
  ADD KEY `city_id` (`city_id`);

--
-- Indexes for table `service_feedback_tbl`
--
ALTER TABLE `service_feedback_tbl`
  ADD PRIMARY KEY (`feedback_id`),
  ADD KEY `feedback_user_id` (`user_id`),
  ADD KEY `feedback_service_book_id` (`service_book_id`);

--
-- Indexes for table `service_list_tbl`
--
ALTER TABLE `service_list_tbl`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `ser_center_id` (`ser_center_id`);

--
-- Indexes for table `states`
--
ALTER TABLE `states`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_addr_tbl`
--
ALTER TABLE `user_addr_tbl`
  ADD PRIMARY KEY (`address_id`),
  ADD KEY `addr_tbl_city_id_fk` (`city_id`),
  ADD KEY `addr_tbl_user_id_fk` (`user_id`);

--
-- Indexes for table `user_tbl`
--
ALTER TABLE `user_tbl`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_tbl_city_id_fk` (`city_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_tbl`
--
ALTER TABLE `admin_tbl`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bike_brand_tbl`
--
ALTER TABLE `bike_brand_tbl`
  MODIFY `brand_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `bike_purchase_tbl`
--
ALTER TABLE `bike_purchase_tbl`
  MODIFY `purchase_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `cities`
--
ALTER TABLE `cities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=604;

--
-- AUTO_INCREMENT for table `contact_tbl`
--
ALTER TABLE `contact_tbl`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `reset_pass_tbl`
--
ALTER TABLE `reset_pass_tbl`
  MODIFY `reset_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `sales_bike_img_tbl`
--
ALTER TABLE `sales_bike_img_tbl`
  MODIFY `image_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `sales_bike_tbl`
--
ALTER TABLE `sales_bike_tbl`
  MODIFY `bike_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `service_book_img_tbl`
--
ALTER TABLE `service_book_img_tbl`
  MODIFY `service_book_img_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `service_book_tbl`
--
ALTER TABLE `service_book_tbl`
  MODIFY `service_book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `service_center_table`
--
ALTER TABLE `service_center_table`
  MODIFY `service_center_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `service_feedback_tbl`
--
ALTER TABLE `service_feedback_tbl`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `service_list_tbl`
--
ALTER TABLE `service_list_tbl`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `states`
--
ALTER TABLE `states`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `user_addr_tbl`
--
ALTER TABLE `user_addr_tbl`
  MODIFY `address_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_tbl`
--
ALTER TABLE `user_tbl`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `bike_purchase_tbl`
--
ALTER TABLE `bike_purchase_tbl`
  ADD CONSTRAINT `purchase_sales_bike_id_fk` FOREIGN KEY (`bike_id`) REFERENCES `sales_bike_tbl` (`bike_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `purchase_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_tbl` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `sales_bike_img_tbl`
--
ALTER TABLE `sales_bike_img_tbl`
  ADD CONSTRAINT `saled_bike_id_fk` FOREIGN KEY (`sales_bike_id`) REFERENCES `sales_bike_tbl` (`bike_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sales_bike_tbl`
--
ALTER TABLE `sales_bike_tbl`
  ADD CONSTRAINT `sales_bike_brand_id_fk` FOREIGN KEY (`brand_id`) REFERENCES `bike_brand_tbl` (`brand_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sales_bike_ser_center_id_fk` FOREIGN KEY (`ser_center_id`) REFERENCES `service_center_table` (`service_center_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `service_book_tbl`
--
ALTER TABLE `service_book_tbl`
  ADD CONSTRAINT `service_book_bike_brand_fk` FOREIGN KEY (`bike_brand_id`) REFERENCES `bike_brand_tbl` (`brand_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `service_book_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_tbl` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `service_center_table`
--
ALTER TABLE `service_center_table`
  ADD CONSTRAINT `service_center_table_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`);

--
-- Constraints for table `service_feedback_tbl`
--
ALTER TABLE `service_feedback_tbl`
  ADD CONSTRAINT `feedback_service_book_id` FOREIGN KEY (`service_book_id`) REFERENCES `service_book_tbl` (`service_book_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `feedback_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_tbl` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `service_list_tbl`
--
ALTER TABLE `service_list_tbl`
  ADD CONSTRAINT `ser_center_id` FOREIGN KEY (`ser_center_id`) REFERENCES `service_center_table` (`service_center_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_addr_tbl`
--
ALTER TABLE `user_addr_tbl`
  ADD CONSTRAINT `addr_tbl_city_id_fk` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `addr_tbl_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_tbl` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_tbl`
--
ALTER TABLE `user_tbl`
  ADD CONSTRAINT `user_tbl_city_id_fk` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
