use std::fmt;
use std::result;

pub type Result<T> = result::Result<T,Error>;

pub fn throw<T>(kind: MrError) -> Result<T> { Err(Error::new(kind)) }

#[derive(Debug)]
pub enum MrError {
	ComposerNotFound,
	ComposerNoExtension,
	ComposerWrongExtension,
	ComposerEmpty,
	ComposerWrongYamlFormat,
	ComposerNoVersion,
	ComposerWrongVersion,

	_Unimplemented
}

impl MrError {
	pub fn as_str(&self) -> &'static str {
		match *self {
			MrError::ComposerNotFound           => "Cannot read the composer (No such file)",
			MrError::ComposerNoExtension        => "The composer has no extension",
			MrError::ComposerWrongExtension     => "The composer has no YAML extension",
			MrError::ComposerEmpty              => "The composer is empty",
			MrError::ComposerWrongYamlFormat    => "YAML syntax error in composer",
			MrError::ComposerNoVersion          => "Numeric attribute 'version' not specified in composer",
			MrError::ComposerWrongVersion       => "Numeric attribute 'version' has a wrong value (should be: 1)",

			MrError::_Unimplemented              => "Error not implemented yet"
		}
	}
}

pub struct Error {
	pub kind: MrError
}
impl From<MrError> for Error {
	fn from(kind: MrError) -> Self {
		Error::new(kind)
	}
}

impl fmt::Debug for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        fmt::Debug::fmt(&self.kind, f)
    }
}

impl Error {
	pub fn new(kind: MrError) -> Error {
		Error { kind }
	}
}

/* Documentation:
	- https://doc.rust-lang.org/src/std/io/error.rs.html
*/