use db_fcsp;
DROP TABLE house_info;


CREATE DATABASE db_fcsp DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use db_fcsp;

CREATE TABLE house_info (
  house_info_id INTEGER AUTO_INCREMENT PRIMARY KEY COMMENT '房屋信息主键',
  community_name VARCHAR(128) COMMENT '小区名称',
  url VARCHAR(128) COMMENT '网页地址',
  title VARCHAR(256) COMMENT '标题信息',
  house_type VARCHAR(64) COMMENT '户型',
  unit_price INTEGER COMMENT '单价',
  total_price INTEGER COMMENT '总价',
  area DOUBLE COMMENT '面积',
  floor VARCHAR(64) COMMENT '楼层',
  heading VARCHAR(64) COMMENT '朝向',
  decoration VARCHAR(64) COMMENT '装修',
  built_year INTEGER COMMENT '建造年份',
  school_names VARCHAR(256) COMMENT '学校学区',
  district VARCHAR(64) COMMENT '所属区域',
  token VARCHAR(64) COMMENT '标识街区',
  metro VARCHAR(64) COMMENT '地铁',
  create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '当前时间',
  update_time TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '房屋信息';

-- TEST
-- INSERT INTO house_info(community_name, url, title, house_type, unit_price, total_price, area, floor, heading, decoration, built_year, school_names, district, token, metro) values ("文化名园碧波阁", "https://nj.lianjia.com/ershoufang/103101396787.html", "文化名园 碧波阁 临湖一幢 居家自住", "3室2厅", 30874, 380, 123.08, "中楼层/共11层", "南 北", "其他", 2008, "", "江宁", "百家湖", "近3号线天元西路站");
