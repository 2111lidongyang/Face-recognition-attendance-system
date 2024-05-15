/*
 Navicat Premium Data Transfer

 Source Server         : team2111
 Source Server Type    : MySQL
 Source Server Version : 80033
 Source Host           : 43.143.229.40:3306
 Source Schema         : face_card

 Target Server Type    : MySQL
 Target Server Version : 80033
 File Encoding         : 65001

 Date: 15/05/2024 22:34:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance
-- ----------------------------
DROP TABLE IF EXISTS `attendance`;
CREATE TABLE `attendance`  (
  `work_id` int NOT NULL COMMENT '工号',
  `time` date NOT NULL COMMENT '日期',
  `state` int NULL DEFAULT NULL COMMENT '考勤状态，0：未签到，1：已签到，2：病假，3：事假，4：迟到',
  `card_time` datetime NULL DEFAULT NULL COMMENT '考勤时间'
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance
-- ----------------------------
INSERT INTO `attendance` VALUES (678, '2024-05-09', 0, NULL);
INSERT INTO `attendance` VALUES (1, '2024-05-09', 4, '2024-05-09 23:57:39');
INSERT INTO `attendance` VALUES (1, '2024-05-10', 1, '2024-05-10 00:03:17');
INSERT INTO `attendance` VALUES (678, '2024-05-10', 0, NULL);
INSERT INTO `attendance` VALUES (2, '2024-05-10', 1, '2024-05-10 00:12:00');
INSERT INTO `attendance` VALUES (2, '2024-05-12', 3, NULL);
INSERT INTO `attendance` VALUES (2, '2024-05-13', 3, NULL);
INSERT INTO `attendance` VALUES (789, '2024-05-10', 4, '2024-05-10 14:17:53');
INSERT INTO `attendance` VALUES (1, '2024-05-11', 0, NULL);
INSERT INTO `attendance` VALUES (2, '2024-05-11', 0, NULL);
INSERT INTO `attendance` VALUES (678, '2024-05-11', 0, NULL);
INSERT INTO `attendance` VALUES (789, '2024-05-11', 0, NULL);
INSERT INTO `attendance` VALUES (1, '2024-05-13', 0, NULL);
INSERT INTO `attendance` VALUES (678, '2024-05-13', 0, NULL);
INSERT INTO `attendance` VALUES (789, '2024-05-13', 0, NULL);
INSERT INTO `attendance` VALUES (21, '2024-05-13', 4, '2024-05-13 15:39:27');
INSERT INTO `attendance` VALUES (1, '2024-05-15', 0, NULL);
INSERT INTO `attendance` VALUES (2, '2024-05-15', 0, NULL);
INSERT INTO `attendance` VALUES (21, '2024-05-15', 4, '2024-05-15 15:17:38');
INSERT INTO `attendance` VALUES (678, '2024-05-15', 0, NULL);
INSERT INTO `attendance` VALUES (789, '2024-05-15', 0, NULL);
INSERT INTO `attendance` VALUES (12, '2024-05-15', 0, NULL);

-- ----------------------------
-- Table structure for check_in
-- ----------------------------
DROP TABLE IF EXISTS `check_in`;
CREATE TABLE `check_in`  (
  `user_id` int NOT NULL COMMENT '用户的id',
  `time` date NOT NULL COMMENT '日期',
  `is_card` int NOT NULL COMMENT '是否签到， 0：未签到 1：签到',
  `card_time` datetime NULL DEFAULT NULL COMMENT '每次打卡的时间'
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of check_in
-- ----------------------------
INSERT INTO `check_in` VALUES (48200, '2024-04-26', 1, '2024-04-26 17:44:23');
INSERT INTO `check_in` VALUES (37880, '2024-04-26', 1, '2024-04-26 18:02:45');
INSERT INTO `check_in` VALUES (37880, '2024-04-29', 0, NULL);
INSERT INTO `check_in` VALUES (48200, '2024-04-29', 0, NULL);
INSERT INTO `check_in` VALUES (241185, '2024-04-29', 1, '2024-04-29 17:04:29');
INSERT INTO `check_in` VALUES (37880, '2024-05-06', 0, NULL);
INSERT INTO `check_in` VALUES (48200, '2024-05-06', 0, NULL);
INSERT INTO `check_in` VALUES (241185, '2024-05-06', 1, '2024-05-06 23:15:50');
INSERT INTO `check_in` VALUES (37880, '2024-05-07', 0, NULL);
INSERT INTO `check_in` VALUES (48200, '2024-05-07', 0, NULL);
INSERT INTO `check_in` VALUES (241185, '2024-05-07', 0, NULL);
INSERT INTO `check_in` VALUES (37880, '2024-05-14', 0, NULL);
INSERT INTO `check_in` VALUES (48200, '2024-05-14', 0, NULL);
INSERT INTO `check_in` VALUES (241185, '2024-05-14', 0, NULL);
INSERT INTO `check_in` VALUES (37880, '2024-05-15', 0, NULL);
INSERT INTO `check_in` VALUES (48200, '2024-05-15', 0, NULL);
INSERT INTO `check_in` VALUES (241185, '2024-05-15', 1, '2024-05-15 22:18:39');

-- ----------------------------
-- Table structure for leave
-- ----------------------------
DROP TABLE IF EXISTS `leave`;
CREATE TABLE `leave`  (
  `work_id` int NOT NULL COMMENT '工号',
  `types_of_leaves` int NOT NULL COMMENT '请假类型，0：病假，1：事假',
  `leave_explanation` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '请假说明',
  `start_time` date NOT NULL COMMENT '开始时间',
  `stop_time` date NOT NULL COMMENT '结束时间'
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of leave
-- ----------------------------
INSERT INTO `leave` VALUES (2, 1, '有事', '2024-05-12', '2024-05-13');

-- ----------------------------
-- Table structure for manager
-- ----------------------------
DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager`  (
  `user_id` varchar(25) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `user_pwd` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of manager
-- ----------------------------
INSERT INTO `manager` VALUES ('12', '12');
INSERT INTO `manager` VALUES ('21', '027221');
INSERT INTO `manager` VALUES ('27221', '27221');
INSERT INTO `manager` VALUES ('333', '333');
INSERT INTO `manager` VALUES ('666', '666');
INSERT INTO `manager` VALUES ('789', '123');
INSERT INTO `manager` VALUES ('888', '888');
INSERT INTO `manager` VALUES ('999', '999');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '用户的名字',
  `user_id` int NOT NULL COMMENT '用户的id',
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('dashafa', 37880);
INSERT INTO `users` VALUES ('a', 48200);
INSERT INTO `users` VALUES ('lidongyang', 241185);

-- ----------------------------
-- Table structure for workers
-- ----------------------------
DROP TABLE IF EXISTS `workers`;
CREATE TABLE `workers`  (
  `work_id` int NOT NULL COMMENT '工号',
  `name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `gender` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '性别',
  `work_age` int NOT NULL COMMENT '工龄',
  `phone` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '电话',
  `department` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '部门',
  `image_url` varchar(25) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '用户照片',
  PRIMARY KEY (`work_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of workers
-- ----------------------------
INSERT INTO `workers` VALUES (1, 'liuxiaofei', '女', 1, '12345232142', '技术', 'face_imageliuxiaofei.png');
INSERT INTO `workers` VALUES (2, 'sunnvshi', '女', 2, '12334214224', '技术', 'face_imagesunnvshi.png');
INSERT INTO `workers` VALUES (12, '12', '12', 12, '12', '12', 'face_image12.png');
INSERT INTO `workers` VALUES (21, 'lu', '男', 22, '15962607953', '软件工程', 'face_imagelu.png');
INSERT INTO `workers` VALUES (678, 'likaier', '男', 3, '19534998872', '技术部', 'face_imagelikaier.png');
INSERT INTO `workers` VALUES (789, 'li', '男', 2, '1234', '销售部', 'face_imageli.png');

SET FOREIGN_KEY_CHECKS = 1;
