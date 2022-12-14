USE [django_administrador]
GO
/****** Object:  Table [dbo].[tlb_member_detail]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tlb_member_detail](
	[detail_id] [int] IDENTITY(1,1) NOT NULL,
	[id_member] [int] NULL,
	[date_bith] [date] NOT NULL,
	[direction] [varchar](250) NULL,
	[Civil_status] [int] NOT NULL,
	[Dependents] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[detail_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tlb_member_email]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tlb_member_email](
	[id_email] [int] IDENTITY(1,1) NOT NULL,
	[id_member] [int] NOT NULL,
	[email] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tlb_member_job]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tlb_member_job](
	[Job_ID] [int] IDENTITY(1,1) NOT NULL,
	[id_member] [int] NULL,
	[id_position] [int] NULL,
	[date_entry] [date] NOT NULL,
	[direction] [varchar](250) NULL,
	[Job_name] [varchar](150) NULL,
PRIMARY KEY CLUSTERED 
(
	[Job_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tlb_member_phone]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tlb_member_phone](
	[id_contact] [int] IDENTITY(1,1) NOT NULL,
	[id_member] [int] NOT NULL,
	[Phone1] [varchar](50) NULL,
	[type_phone] [varchar](50) NULL,
	[status_fone] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_contact] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tlb_members]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tlb_members](
	[id_member] [int] NOT NULL,
	[member_name] [varchar](100) NOT NULL,
	[status_memb] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_member] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tlb_status_Civil]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tlb_status_Civil](
	[id_civilstatus] [int] IDENTITY(1,1) NOT NULL,
	[Desc_civil] [varchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_civilstatus] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[tlb_member_detail]  WITH CHECK ADD  CONSTRAINT [fk_Civil_status] FOREIGN KEY([Civil_status])
REFERENCES [dbo].[tlb_status_Civil] ([id_civilstatus])
GO
ALTER TABLE [dbo].[tlb_member_detail] CHECK CONSTRAINT [fk_Civil_status]
GO
ALTER TABLE [dbo].[tlb_member_detail]  WITH CHECK ADD  CONSTRAINT [fk_member_detail] FOREIGN KEY([id_member])
REFERENCES [dbo].[tlb_members] ([id_member])
GO
ALTER TABLE [dbo].[tlb_member_detail] CHECK CONSTRAINT [fk_member_detail]
GO
ALTER TABLE [dbo].[tlb_member_email]  WITH CHECK ADD  CONSTRAINT [fk_member_email] FOREIGN KEY([id_member])
REFERENCES [dbo].[tlb_members] ([id_member])
GO
ALTER TABLE [dbo].[tlb_member_email] CHECK CONSTRAINT [fk_member_email]
GO
ALTER TABLE [dbo].[tlb_member_job]  WITH CHECK ADD  CONSTRAINT [fk_job_Position] FOREIGN KEY([id_position])
REFERENCES [dbo].[tlb_job_Position] ([id_position])
GO
ALTER TABLE [dbo].[tlb_member_job] CHECK CONSTRAINT [fk_job_Position]
GO
ALTER TABLE [dbo].[tlb_member_job]  WITH CHECK ADD  CONSTRAINT [fk_member_job] FOREIGN KEY([id_member])
REFERENCES [dbo].[tlb_members] ([id_member])
GO
ALTER TABLE [dbo].[tlb_member_job] CHECK CONSTRAINT [fk_member_job]
GO
ALTER TABLE [dbo].[tlb_member_phone]  WITH CHECK ADD  CONSTRAINT [fk_contact] FOREIGN KEY([id_member])
REFERENCES [dbo].[tlb_members] ([id_member])
GO
ALTER TABLE [dbo].[tlb_member_phone] CHECK CONSTRAINT [fk_contact]
GO
ALTER TABLE [dbo].[tlb_member_email]  WITH CHECK ADD  CONSTRAINT [CHK_ColumnD_DocExc] CHECK  (([email] like '%_@__%.__%'))
GO
ALTER TABLE [dbo].[tlb_member_email] CHECK CONSTRAINT [CHK_ColumnD_DocExc]
GO
/****** Object:  StoredProcedure [dbo].[SP_INSERT_MEMBER]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:		<Rios,Gaston>
-- Create date: <09/09/2022>
-- Description:	<SP>
-- =============================================
CREATE PROCEDURE [dbo].[SP_INSERT_MEMBER]
@MEMBER_ID VARCHAR (50),
@MEMBER_NAME VARCHAR (100)
AS
BEGIN
	
SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')

 IF NOT EXISTS (SELECT TOP 1 * FROM [dbo].[tlb_members] WHERE id_member = @MEMBER_ID )
	BEGIN 
		INSERT INTO [dbo].[tlb_members] ([id_member],[member_name],[status_memb]) VALUES (@MEMBER_ID,@MEMBER_NAME,1)
	END
ELSE
	BEGIN
		DECLARE @ERROR_MESSAGE	NVARCHAR(4000)
		SET @ERROR_MESSAGE='Member already exists in the database'
		RAISERROR(@ERROR_MESSAGE, 16, 1)
	END

END
GO
/****** Object:  StoredProcedure [dbo].[SP_INSERT_MEMBER_DETAIL]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO



-- =============================================
-- Author:		<Rios,Gaston>
-- Create date: <09/09/2022>
-- Description:	<SP>
-- =============================================
CREATE PROCEDURE [dbo].[SP_INSERT_MEMBER_DETAIL]
@MEMBER_ID VARCHAR(50),
@date_bith VARCHAR(100),
@direction VARCHAR (250),
@Civil_status INT,
@Dependents INT
AS
BEGIN
	
SET @MEMBER_ID = convert(int,REPLACE(@MEMBER_ID,'-',''))
SET @date_bith = CONVERT(date,@date_bith,103)


 IF EXISTS (SELECT TOP 1 * FROM [dbo].[tlb_members] WHERE id_member = @MEMBER_ID )
	BEGIN 
		DECLARE @COUNT INT
	    SELECT @COUNT = COUNT(*) FROM [dbo].[tlb_member_detail] WHERE id_member = @MEMBER_ID 
		IF @COUNT = 0
			BEGIN
				INSERT INTO [dbo].[tlb_member_detail]  VALUES (@MEMBER_ID,@date_bith,@direction,@Civil_status,@Dependents)
			END
		ELSE
			BEGIN
				UPDATE [dbo].[tlb_member_detail] SET date_bith= @date_bith, direction = @direction , Civil_status = @Civil_status , Dependents = @Dependents WHERE id_member = @MEMBER_ID
			END
	END
ELSE
	BEGIN
		DECLARE @ERROR_MESSAGE	NVARCHAR(4000)
		SET @ERROR_MESSAGE='Member does not exist in the database'
		RAISERROR(@ERROR_MESSAGE, 16, 1)
	END

END
GO
/****** Object:  StoredProcedure [dbo].[SP_INSERT_MEMBER_EMAIL]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:		<Rios,Gaston>
-- Create date: <09/09/2022>
-- Description:	<SP>
-- =============================================
CREATE PROCEDURE [dbo].[SP_INSERT_MEMBER_EMAIL]
@MEMBER_ID VARCHAR(50),
@EMAIL VARCHAR(100)
AS
BEGIN
	
SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')

 IF EXISTS (SELECT TOP 1 * FROM [dbo].[tlb_members] WHERE id_member = @MEMBER_ID )
	BEGIN 
		INSERT INTO [dbo].[tlb_member_email] VALUES (@MEMBER_ID,@EMAIL)
	END
ELSE
	BEGIN
		DECLARE @ERROR_MESSAGE	NVARCHAR(4000)
		SET @ERROR_MESSAGE='Member does not exist in the database'
		RAISERROR(@ERROR_MESSAGE, 16, 1)
	END

END
GO
/****** Object:  StoredProcedure [dbo].[SP_INSERT_MEMBER_JOB]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:		<Rios,Gaston>
-- Create date: <09/09/2022>
-- Description:	<SP>
-- =============================================
CREATE PROCEDURE [dbo].[SP_INSERT_MEMBER_JOB]
@MEMBER_ID VARCHAR(50),
@ID_POSITION INT,
@date_entry VARCHAR(100),
@direction_job VARCHAR (250),
@job_name VARCHAR (250)
AS
BEGIN
	
SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')
SET @date_entry = CONVERT(date,@date_entry,103)

 IF EXISTS (SELECT TOP 1 * FROM [dbo].[tlb_members] WHERE id_member = @MEMBER_ID )
	BEGIN 
		INSERT INTO [dbo].[tlb_member_job] VALUES (@MEMBER_ID,@ID_POSITION,@date_entry,@direction_job,@job_name)
	END
ELSE
	BEGIN
		DECLARE @ERROR_MESSAGE	NVARCHAR(4000)
		SET @ERROR_MESSAGE='Member does not exist in the database'
		RAISERROR(@ERROR_MESSAGE, 16, 1)
	END

END
GO
/****** Object:  StoredProcedure [dbo].[SP_INSERT_MEMBER_Phone]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO




-- =============================================
-- Author:		<Rios,Gaston>
-- Create date: <09/09/2022>
-- Description:	<SP>
-- =============================================
CREATE PROCEDURE [dbo].[SP_INSERT_MEMBER_Phone]
@MEMBER_ID VARCHAR(50),
@phone VARCHAR(50),
@type_phone VARCHAR (250),
@status_phone INT
AS
BEGIN
	
SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')
SET @phone = REPLACE(@phone,'-','')

 IF EXISTS (SELECT TOP 1 * FROM [dbo].[tlb_members] WHERE id_member = @MEMBER_ID )
	BEGIN 
		INSERT INTO [dbo].[tlb_member_contact]  VALUES (@MEMBER_ID,@phone,@type_phone,@status_phone)
	END
ELSE
	BEGIN
		DECLARE @ERROR_MESSAGE	NVARCHAR(4000)
		SET @ERROR_MESSAGE='Member does not exist in the database'
		RAISERROR(@ERROR_MESSAGE, 16, 1)
	END

END
GO
/****** Object:  StoredProcedure [dbo].[SP_LIST_MEMBERS]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[SP_LIST_MEMBERS]
AS
BEGIN
	SET NOCOUNT ON;

	SELECT M.id_member,M.member_name,MD.date_bith,
		   MD.direction,MD.Dependents,
		   SC.Desc_civil,ME.email,MJ.Job_name,
		   MJ.direction,MJ.date_entry,JP.Desc_position,
		   MP.Phone1,MP.type_phone
	FROM [dbo].[tlb_members] AS M
	INNER JOIN [dbo].[tlb_member_detail] AS MD ON M.[id_member] = MD.id_member
	INNER JOIN [dbo].[tlb_member_email] AS ME ON M.[id_member] = ME.id_member
	INNER JOIN [dbo].[tlb_member_job] AS MJ ON M.[id_member] = MJ.id_member
	INNER JOIN [dbo].[tlb_member_phone] AS MP ON M.[id_member] = MP.id_member
	INNER JOIN [dbo].[tlb_status_Civil] AS SC ON SC.id_civilstatus = MD.Civil_status
	INNER JOIN [dbo].[tlb_job_Position] AS JP ON JP.id_position = MJ.id_position

END
GO
/****** Object:  StoredProcedure [dbo].[SP_NEW_MEMBER]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[SP_NEW_MEMBER]
@MEMBER_ID VARCHAR (50),
@MEMBER_NAME VARCHAR (100),
@date_bith VARCHAR(100),
@direction VARCHAR (250),
@Civil_status INT,
@Dependents INT,
@EMAIL VARCHAR(100),
@ID_POSITION INT,
@date_entry VARCHAR(100),
@direction_JOB VARCHAR (250),
@job_name VARCHAR (250),
@phone VARCHAR(50),
@type_phone VARCHAR (250),
@status_phone INT
AS
BEGIN
	SET NOCOUNT ON;
	SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')

	 IF EXISTS (SELECT TOP 1 * FROM [dbo].[tlb_members] WHERE id_member = @MEMBER_ID )
		BEGIN 
			DECLARE @ERROR_MESSAGE	NVARCHAR(4000)
			SET @ERROR_MESSAGE='Member already exists in the database'
			RAISERROR(@ERROR_MESSAGE, 16, 1)
		END
	 ELSE
		BEGIN
			-- Components ---
			EXEC [dbo].[SP_INSERT_MEMBER] @MEMBER_ID, @MEMBER_NAME
			EXEC [dbo].[SP_INSERT_MEMBER_DETAIL] @MEMBER_ID, @date_bith, @direction , @Civil_status, @Dependents
			EXEC [dbo].[SP_INSERT_MEMBER_EMAIL] @MEMBER_ID, @EMAIL
			EXEC [dbo].[SP_INSERT_MEMBER_JOB] @MEMBER_ID, @ID_POSITION, @date_entry, @direction_JOB, @job_name
			EXEC [dbo].[SP_INSERT_MEMBER_Phone] @MEMBER_ID, @phone, @type_phone, @status_phone
		END
END
GO
/****** Object:  StoredProcedure [dbo].[SP_SHOW_MEMBER]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[SP_SHOW_MEMBER]
@MEMBER_ID VARCHAR (50)
AS

BEGIN
	SET NOCOUNT ON;

	SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')

	SELECT M.id_member,M.member_name,MD.date_bith,
		   MD.direction,MD.Dependents,
		   SC.Desc_civil,ME.email,MJ.Job_name,
		   MJ.direction,MJ.date_entry,JP.Desc_position,
		   MP.Phone1,MP.type_phone
	FROM [dbo].[tlb_members] AS M
	INNER JOIN [dbo].[tlb_member_detail] AS MD ON M.[id_member] = MD.id_member
	INNER JOIN [dbo].[tlb_member_email] AS ME ON M.[id_member] = ME.id_member
	INNER JOIN [dbo].[tlb_member_job] AS MJ ON M.[id_member] = MJ.id_member
	INNER JOIN [dbo].[tlb_member_phone] AS MP ON M.[id_member] = MP.id_member
	INNER JOIN [dbo].[tlb_status_Civil] AS SC ON SC.id_civilstatus = MD.Civil_status
	INNER JOIN [dbo].[tlb_job_Position] AS JP ON JP.id_position = MJ.id_position
	WHERE M.id_member = @MEMBER_ID

END
GO
/****** Object:  StoredProcedure [dbo].[SP_SHOW_MEMBER_JSON]    Script Date: 16/09/2022 21:33:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO



-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[SP_SHOW_MEMBER_JSON]
@MEMBER_ID VARCHAR (50)
AS

BEGIN
	SET NOCOUNT ON;

	SET @MEMBER_ID = REPLACE(@MEMBER_ID,'-','')

	SELECT M.id_member AS DNI
	,M.member_name AS NOMBRE_APELLIDO
	,MD.date_bith AS FECHA_NACIMIENTO
	,MD.direction AS DOMICILIO
	,MD.Dependents AS HIJOS
	,SC.Desc_civil AS ESTADO_CIVIL
	,ME.email AS EMAIL
	,MJ.Job_name AS NOMBRE_EMPLEO
	,MJ.direction AS DIRECCION_EMPLEO
	,MJ.date_entry AS FECHA_INGRESO
	,JP.Desc_position AS POSICION
	,MP.Phone1 AS TELEFONO
	,MP.type_phone AS TIPO_TELEFONO
	FROM [dbo].[tlb_members] AS M
	INNER JOIN [dbo].[tlb_member_detail] AS MD ON M.[id_member] = MD.id_member
	INNER JOIN [dbo].[tlb_member_email] AS ME ON M.[id_member] = ME.id_member
	INNER JOIN [dbo].[tlb_member_job] AS MJ ON M.[id_member] = MJ.id_member
	INNER JOIN [dbo].[tlb_member_phone] AS MP ON M.[id_member] = MP.id_member
	INNER JOIN [dbo].[tlb_status_Civil] AS SC ON SC.id_civilstatus = MD.Civil_status
	INNER JOIN [dbo].[tlb_job_Position] AS JP ON JP.id_position = MJ.id_position
	WHERE M.id_member = @MEMBER_ID
	FOR JSON PATH

END
GO
